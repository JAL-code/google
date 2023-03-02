# Regex checks alternates for group headings, item name and acronym (gm omitted)
# original:  r"^(\#)|(\*)+ Level ([\w \.]*)|([\w \.]*)+|\(([\w \.]*)\)$"
# complex:  r"^(\#)|(?P<level>  (\*)+ Level ([\w \.]*))|(?P<source>  0 Sources)|(?P<name>   ([\w \.|-]*)+)|(?P<acronym>:\s{2}\(([\w \.]*)\))$"
# final:  r"^(\#)|(?P<level>  (\*)+ Level ([\w \.]*))|(?P<source>  0 Sources)|(?P<name>   ([\w \.\-\(\)]*)+)|(?P<acronym>:\s{2}\(([\w \.]*)\))$"
# List of components and products
#  0 Sources
#   Copper vein:  (CV)
#   Iron vein:  (IV)
#   Stone vein:  (SV)
#   Silicon vein:  (SiV)
#   Fractal silicon vein:  (FSiV)
#   Star:  (ST)
#   Crude oil vein:  (CoilV)
#   Ice giant:  (ICE)
#   Fire ice vein:  (FIV)
#   Coal vein:  (CLV)
#   Gas giant:  (GAS)
#   Optical grating rock vein:  (OPRV)
#   Titanium vein:  (TiV)
#   Sulfur sea:  (SS)
#   Water sea:  (WS)
#   Organic crystal vein:  (OCV)
#   Kimberlite vein:  (KiV)
#   Spiniform stalagmite crystal vein:  (SpSCV)
#  * Level one
#   Copper ore:  (Cor)
#   Iron ore:  (Ior)
#   Stone:  (Stn)
#   Silicon ore:  (Sior)
#   Fractal silicon:  (FS)
#   Unipolar magnet:  (UM)
#   Crude oil:  (Coil)
#   Fire ice:  (FI)
#   Coal:  (CL)
#   Optical grating crystal:  (OGC)
#   Titanium ore:  (Tior)
#   Water:  (H20)
#   Plant fuel:  (PF)
#   Log:  (L)
#   Kimberlite ore:  (Kior)
#   Spiniform stalagmite crystal:  (SpSC)
#  ** Level two
#   Iron ingot:  (IIn)
#   Copper ingot:  (CIn)
#   High-purity silicon:  (HPSi)
#   Stone brick:  (SBr)
#   Glass:  (Gl)
#   Steel:  (STL)
#   Magnet:  (Mag)
#   Prism:  (Psm)
#   Crystal silicon:  (CrySi)
#   Critical photon:  (CriPh)
#   Refined oil:  (Roil)
#   Hydrogen:  (H)
#   Energetic graphite:  (EGr)
#   Graphene:  (Grph)
#   Deuterium:  (Deut)
#   Titanium ingot:  (TiIn)
#   Sulfuric acid:  (SA)
#   Strange matter:  (SM)
#   Plastic:  (Plst)
#   Titanium glass:  (TiGl)
#   Organic crystal:  (OrCry)
#   Titanium crystal:  (TiCry)
#   Casimir crystal:  (CaCry)
#   Diamond:  (Dia)
#   Carbon nanotube:  (CaNano)
#   Antimatter:  (Anti)
#   Titanium alloy:  (TiAll)
#   Frame material:  (Fram)
#  *** Level three
#   Electromagnetic matrix:  (ElMa)
#   Energy matrix:  (EnMa)
#   Solar sail:  (Solar)
#   Hydrogen fuel rod:  (HyFR)
#   Information matrix:  (IM)
#   Deuteron fuel rod:  (DeutFR)
#   Structure matrix:  (SMa)
#   Gravity matrix:  (GMa)
#   Universe matrix:  (MMa)
#   Small carrier rocket:  (SCR)
#   Antimatter fuel rod:  (AntiFR)
#  **** Level four
#   Gear:  (GR)
#   Magnetic coil:  (MagCoil)
#   Circuit board:  (PCB)
#   Electric motor:  (EM)
#   Microcrystalline component:  (MICRO)
#   Thruster:  (THR)
#   Electromagnetic turbine:  (EMT)
#   Foundation:  (FDT)
#   Plasma exciter:  (PLE)
#   Photon combiner:  (PHCB)
#   Particle container:  (ParCT)
#   Processor:  (Proc)
#   Super-magnetic ring:  (SMagR)
#   Particle broadband:  (PartBB)
#   Plane filter:  (PlnF)
#   Graviton lens:  (GravLn)
#   Dyson sphere component:  (DSC)
#   Space warper:  (SpW)
#   Quantum chip:  (QCh)
#   Annihilation constraint sphere:  (ACS)
#   Reinforced thruster:  (ReT)
#  **** Level five
#   Wind turbine:  (WTur)
#   Assembling machine Mk.I:  (AMkI)
#   Mining machine:  (Mine)
#   Tesla tower:  (Tesla)
#   Thermal power plant:  (TPP)
#   Solar panel:  (SolPP)
#   Matrix lab:  (MatLab)
#   Arc Smelter:  (ArcSmel)
#   Water pump:  (WPp)
#   Chemical plant:  (ChPl)
#   Oil extractor:  (OilX)
#   Oil refinery:  (OilR)
#   Wireless power tower:  (WPT)
#   Fractionator:  (Frac)
#   EM-Rail Ejector:  (EmRailEj)
#   Accumulator:  (Accum)
#   Ray receiver:  (Ray)
#   Energy exchanger:  (EnEx)
#   Assembling machine Mk.II:  (AMkII)
#   Miniature particle collider:  (MPC)
#   Mini fusion power plant:  (MiniFPP)
#   Satellite substation:  (SatSub)
#   Assembling machine Mk.III:  (AMkIII)
#   Plane Smelter:  (PlaneSm)
#   Vertical launching silo:  (VertSilo)
#   Accumulator (full):  (AccumF)
#   Artifical star:  (ArtStr)
#  ***** Level six
#   Splitter:  (Split)
#   Conveyer belt MK.I:  (CBMkI)
#   Sorter MK.I:  (SortMkI)
#   Sorter MK.II:  (SortMkII)
#   Storage MK.I:  (StoreMkI)
#   Logistics drone:  (LogDrn)
#   Storage tank:  (StrTnk)
#   Sorter MK.III:  (SortMkII)
#   Conveyor belt MK.II:  (CBMkII)
#   Storage MK.II:  (StoreMkII)
#   Conveyor belt MK.III:  (CBMkIII)
#   Planetory Logistics Station:  (PlaLog)
#   Interstellar Logistics Station:  (InterLog)
#   Orbital Collector:  (OrbClct)
#   Logistics vessel:  (LogVes)
#   ITEMS: 136
#   Properties (By Node)
#           Research Facility [N_RF]:  Name, Picture, Stack Size, Assembler speed, Work consumption, Idle consumption, Flags, [Recipe], [Action Type]
#           Logistics [N_L]:                  Name, Picture, Stack Size, Technology, Flags, [Recipes], Used In, [Belt speed, Work consumption, Idle Consumption, Cells, Volume, Can Accumulate, Max Drones, Max Items, Item Types, Max Ships]
#           Chemical Facility [N_CF]:          Name, Picture, Stack Size, Assembler speed, Work consumption, Idle consumption, Flags, [Recipe], [Action Type]
#           Assembler [N_A]:                  Name, Picture, Stack Size, Assembler speed, Work consumption, Idle consumption, Technology, Flags, [Recipe], [Used In], [Action Type]
#           Oil Extraction Facility [N_OEF]:    Name, Picture, Stack Size, Assembler speed, Work consumption, Idle consumption, Flags, [Recipe], [Action Type]
#           Refining Facility [N_RF]:          Name, Picture, Stack Size, Assembler speed, Work consumption, Idle consumption, Flags, [Recipe], [Action Type]
#           Mining Facility [N_MF]:            Name, Picture, Stack Size, Assembler speed, Work consumption, Idle consumption, Flags, [Recipe], [Action Type]
#           Power Facility [N_PF]:             Name, Picture, Stack Size, Power connect, Power radius, Generate energy, Technology, Flags, [Recipe], [Action Type]
#           End Product [N_EP]:                Name, Picture, Energy, Flags, [Recipes], [Used In]
#           Power Storage [N_PS]:              Name, Picture, Stack Size, Power Connect, Energy, Flags, [Recipes], [Used in]
#           FluidVein [N_FV]:                  Name, Picture, Used In, Stack Size, [Recipes], [Action Type]
#           Science Matrix [N_SM]:             Name, Picture, Color, Stack Size, [Recipes], [Used in]
#           Technology [N_T]:                 Name, Picture, Hashes, [Unlock], [Resources], [Action Type]
#           Power Transmission [N_PT]:         Name, Picture, Power connect, Power radius, Technology, Flags, [Recipe], [Used In], [Action Type]
#           Smelting Facility [N_SF]:          Name, Picture, Stack Size, Assembler Speed, Work Consumption, Idle Consumption, Flags, [Recipe]
#           Production Facility [N_PF]:        Name, Picture, Stack Size, Work consumption, Idle consumption, Flags, [Recipe]
#           Water Pumping Facility [N_WPF]:     Name, Picture, Stack Size, Assembler Speed, Work Consumption, Idle Consumption, Flags, [Recipe]
#           Fractionation Facility [N_FF]:     Name, Picture, Stack Size, Assembler speed, Work consumption, Idle consumption, Flags, [Recipe]
#           Component [N_FF]:                  Name, Picture, Stack size, Flags, [Recipes], [Action Type]
#           Particle Collider [N_PC]:          Name, Picture, Stack Size, Assembler speed, Work consumption, Idle consumption, Flags, [Recipe]
#           Natural Resource [N_NR]:           Name, Picture, Used In, NodeType, Stack size, Energy, Flags, NodeType, Production, [Recipes],  [Used In], [Action Type]
#           Vein [N_V]:                       Name, Picture, Used In, NodeType, [Action Type]
#           Material [N_M]:                   Name, Picture, Stack size, Flags, [Recipes], Used In, [Action Type]
# $$ Action Type 
#   PowerTransfer
#   MineDrill
#   Smelt 
#   Pump 
#   PhotonCatch 
#   Refine 
#   Particle 
#   Research resource
#   MineFluidExtractor 
#   Fractionate 
#   Research 
#   OrbitCollector 
#   Assemble
#   Chemical 
#   Unlock
#   Technology Relation
# && Recipe: production   {"<sub-component acronym>":<quanity>, . . . "resultant": <quanity>}
## production:  {"name":<facility acronym>, "time": <seconds>, "MK1": <speed>, "MK2": <speed>, "MK3": <speed>} 
## Unlock: {"unlock": <list of components unlocked>}
## Used In: Create macro to build list of items
## Resources Array: [Matrix Items]  {'Information':<quanity>, 'Universe':<quanity>, 'Gravity':<quanity>, 'Energy':<quanity>, 'Electromagnetic':<quanity>, 'Structure':<quanity>}

# Number of items, Used In, Matrix Items, production: Name, Picture or Ac.
