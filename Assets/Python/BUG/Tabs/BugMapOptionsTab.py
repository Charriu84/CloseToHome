## BugMapOptionsTab
##
## Tab for the BUG Map Options.
##
## Copyright (c) 2009 The BUG Mod.
##
## Author: EmperorFool

import BugOptionsTab

class BugMapOptionsTab(BugOptionsTab.BugOptionsTab):
    "BUG Nap Options Screen Tab"
    
    def __init__(self, screen):
        BugOptionsTab.BugOptionsTab.__init__(self, "Map", "Map")

    def create(self, screen):
        tab = self.createTab(screen)
        panel = self.createMainPanel(screen)
        column = self.addOneColumnLayout(screen, panel)
        
        left, center, right = self.addThreeColumnLayout(screen, column, "Top", True)
        self.createStrategyLayerPanel(screen, left)
        self.createCityBarPanel(screen, center)
        self.createTileHoverPanel(screen, center)
        self.createMiscellaneousPanel(screen, right)
        
        screen.attachHSeparator(column, column + "Sep1")
        self.createCityTileStatusPanel(screen, column)
        
        
    def createStrategyLayerPanel(self, screen, panel):
        self.addLabel(screen, panel, "StrategyOverlay", "Strategy Layer:")
        self.addCheckbox(screen, panel, "StrategyOverlay__Enabled")
        self.addCheckbox(screen, panel, "StrategyOverlay__ShowDotMap")
        self.addCheckbox(screen, panel, "StrategyOverlay__DotMapDrawDots")
        left, right = self.addTwoColumnLayout(screen, panel, "DotMapBrightness")
        #self.addTextEdit(screen, left, right, "StrategyOverlay__DotMapDotIcon")
        self.addSlider(screen, left, right, "StrategyOverlay__DotMapBrightness", False, False, False, "up", 0, 100)
        self.addSlider(screen, left, right, "StrategyOverlay__DotMapHighlightBrightness", False, False, False, "up", 0, 100)
        
    def createCityBarPanel(self, screen, panel):
        self.addLabel(screen, panel, "CityBar", "CityBar:")
        self.addCheckbox(screen, panel, "CityBar__AirportIcons")
        self.addCheckbox(screen, panel, "CityBar__StarvationTurns")
        
    def createTileHoverPanel(self, screen, panel):
        self.addLabel(screen, panel, "TileHover", "Tile Hover:")
        self.addCheckbox(screen, panel, "MiscHover__PlotWorkingCity")
        self.addCheckbox(screen, panel, "MiscHover__PlotRecommendedBuild")
        self.addCheckbox(screen, panel, "MiscHover__PartialBuilds")
        
    def createMiscellaneousPanel(self, screen, panel):
        self.addLabel(screen, panel, "Misc", "Misc:")
        self.addCheckbox(screen, panel, "MainInterface__FieldOfView")
        self.addCheckbox(screen, panel, "MainInterface__FieldOfView_Remember", True)
        self.addCheckbox(screen, panel, "MiscHover__RemoveFeatureHealthEffects")
        self.addCheckbox(screen, panel, "MiscHover__RemoveFeatureHealthEffectsCountOtherTiles", True)
        
    def createCityTileStatusPanel(self, screen, panel):
        left, center, right = self.addThreeColumnLayout(screen, panel, "CityPlotsEnabled", True)
        self.addLabel(screen, left, "CityPlots", "City Tiles:")
        self.addCheckbox(screen, center, "CityBar__CityControlledPlots")
        self.addCheckbox(screen, right, "CityBar__CityPlotStatus")
        
        one, two, three, four, five = self.addMultiColumnLayout(screen, panel, 5, "CityPlotsOptions")
        self.addLabel(screen, one, "WorkingPlots", "Working:")
        self.addCheckbox(screen, two, "CityBar__WorkingImprovedPlot")
        self.addCheckbox(screen, three, "CityBar__WorkingImprovablePlot")
        self.addCheckbox(screen, four, "CityBar__WorkingImprovableBonusPlot")
        self.addCheckbox(screen, five, "CityBar__WorkingUnimprovablePlot")
        self.addLabel(screen, one, "NotWorkingPlots", "Not Working:")
        self.addCheckbox(screen, two, "CityBar__NotWorkingImprovedPlot")
        self.addCheckbox(screen, three, "CityBar__NotWorkingImprovablePlot")
        self.addCheckbox(screen, four, "CityBar__NotWorkingImprovableBonusPlot")
        self.addCheckbox(screen, five, "CityBar__NotWorkingUnimprovablePlot")
        
        #left, right = self.addTwoColumnLayout(screen, column, "MapFinderEnabled", True)
        #self.addLabel(screen, left, "MapFinder", "MapFinder:")
        #self.addCheckbox(screen, right, "MapFinder__Enabled")
        
        #self.addTextEdit(screen, column, column, "MapFinder__Path")
        #self.addTextEdit(screen, column, column, "MapFinder__SavePath")
        
        #left, right = self.addTwoColumnLayout(screen, column, "MapFinder", True)
        #leftL, leftR = self.addTwoColumnLayout(screen, left, "MapFinderDelays")
        #self.addFloatDropdown(screen, leftL, leftR, "MapFinder__RegenerationDelay")
        #self.addFloatDropdown(screen, leftL, leftR, "MapFinder__SkipDelay")
        #self.addFloatDropdown(screen, leftL, leftR, "MapFinder__SaveDelay")
        
        #rightL, rightR = self.addTwoColumnLayout(screen, right, "MapFinderLimits")
        #self.addTextEdit(screen, rightL, rightR, "MapFinder__RuleFile")
        #self.addTextEdit(screen, rightL, rightR, "MapFinder__RegenerationLimit")
        #self.addTextEdit(screen, rightL, rightR, "MapFinder__SaveLimit")
