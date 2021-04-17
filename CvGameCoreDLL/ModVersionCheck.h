//Just include this into CvGameTextMgr.cpp
#pragma once

static const void *CriticalParent_LeaderSelectionScreen = (void*) 0x00524916;

/* This address holds the first civ description string of the network package
 * during the login. It is an address directly in the game binary.
 *
 * => Thus, that assumption only hold for the normal/old civ4bts executable and
 * not in general.
 */
static const void * const Magick_Address = (void*) 0x00BD2369; // Assume length information for wchar here.

static unsigned char checksum_name1[METADATA_MIN_LEN] = { 0 };
static unsigned char checksum_name2[METADATA_MIN_LEN] = { 0 };
static unsigned char checksum_version1[METADATA_MIN_LEN] = { 0 };
static unsigned char checksum_version2[METADATA_MIN_LEN] = { 0 };

void gen_local_checksums(){
	static bool __local_checksums_done = false;
	if (!__local_checksums_done){
		gen_modname_checksum(checksum_name1, false);
		gen_modversion_checksum(checksum_version1);
		__local_checksums_done = true;
	}
}

bool parse_net_checksums(){

	const unsigned char *data = (const unsigned char *)Magick_Address;

	// Loop over all player names. Search first non-empty entry
	// and parse content.
	int iID = -1;
	for( int i=0; i<MAX_CIV_PLAYERS; ++i ){
		int wchar_len = *((int *) (data));
		int avail_len = wchar_len;
		if( wchar_len > 0 && iID == -1){

			iID = i;
			const unsigned char *ws = (data+4+1); //+1 because data is in second byte of wchar

			// Skip normal data
			while (avail_len > 0 && *(ws-1) != '\b' ) {
				ws += 2;
				avail_len -= 1;
			}
			if (avail_len < METADATA_MIN_LEN ){
				// Hey, this can not be the correct message
				return false;
			}

			// Copy data
			for( int j=0; j<METADATA_MIN_LEN; ++j){
				checksum_name2[j] = *ws;
				ws += 2;
			}
		}

		// go to next player string. Required for next step to do this for all players.
		data += sizeof(wchar_t) * wchar_len + 4;
	}

	if( iID == -1 ){
		// If all player slots are consumed on the server this may happen.
		return false;
	}


	// Loop over all civ names and search first non-empty entry
	for( int i=0; i<MAX_CIV_PLAYERS; ++i ){
		int wchar_len = *((int *) (data));
		if( wchar_len > 0){

			const unsigned char *ws = (data+4+1); //+1 because data is in second byte of wchar

			// Here, the metadata prefixes the normal data. No shift needed
			// pointer reached metadata. Check if still enough chars available.
			if (wchar_len < METADATA_MIN_LEN ){
				// Hey, this can not be the correct message
				return false;
			}
			for( int j=0; j<METADATA_MIN_LEN; ++j){
				checksum_version2[j] = *ws;
				ws += 2;
			}
			return true;
		}

		// go to next player string. Required for next step to do this for all players.
		data += sizeof(wchar_t) * wchar_len + 4;
	}

	return false;
}

int compare_checksums(){

	int status_flags = 0;

	// check Password protection flag
	if (checksum_name2[0] == 255 ){
		status_flags |= 4;
	}

	// check mod name
	for( int j=1; j<METADATA_MIN_LEN; ++j){
		if (!(checksum_name1[j] == checksum_name2[j])){
			status_flags |= 2;
		}
	}

	// check mod version
	for( int j=0; j<METADATA_MIN_LEN; ++j){
		if (!(checksum_version1[j] == checksum_version2[j])){
			status_flags |= 1;
		}
	}

	return status_flags;
}

void generate_mod_checksum_popup(int status){
	// I do not know how to show a popup in the main menu directly.
	// So I just call a python function.
	long iResult;
	CyArgsList argsList;
	argsList.add(status);
	gDLL->getPythonIFace()->callFunction("CvScreensInterface", "showModChecksumPopup",
			argsList.makeFunctionArgs(), &iResult);
}

