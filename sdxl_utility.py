
# Converting the prompt generation script into a ComfyUI plugin structure
import random
import nodes

class PromptGenerator:
	RETURN_TYPES = ("STRING",)
	FUNCTION = "generate_prompt"
	CATEGORY = "PromptGenerator"
	@classmethod
	def IS_CHANGED(cls):
			return float("NaN")
	
	@classmethod
	def INPUT_TYPES(cls):
		return {
			"required": {
					"subject": ("STRING", {}),
					},
				}
	
	def generate_prompt(self, subject):
		INITIAL_DESCRIPTION = [
			"self portrait",
			"street portrait",
			"half-body portrait",
			"close up portrait",
			"face shot portrait",
			"studio portrait",
			"glamour close up portrait",
			"fine art close up portrait",
			"Traditional posed portrait",
			"candid portrait",
			"environmental portrait",
			"lifestyle portrait",
			"documentary portrait",
			"black and white portrait",
			"color portrait",
			"beauty portrait",
			"glamour portrait",
			"fine art portrait",
			"fashion portrait",
			"high key portrait",
			"low key portrait",
			"street portrait",
			"self portrait",
		]

		EMOTIONS = [
			"beautiful",
			"glad",
			"sad",
			"angry",
			"neutral"
		]

		DEFAULT_TAGS = [
			"man",
			"woman",
			"young man",
			"young woman",
			"middle aged man",
			"middle aged woman",
		]

		ROLES = [
			"as a ((cyborg))",
			"as an ((x-men character))",
			"as a ((marvel character))",
			"as a ((character from lord of the rings))",
			"as a ((superhero character))",
			"as a ((scifi character))",
			"as a ((character from star wars))",
			"as a ((character from star trek))",
			"as a ((character from the matrix))",
			"as a ((character from the tv show the boys))",
			"as a ((glamour model))",
			"as a ((fashion model))",
			"as a ((greek god))",
			"as a ((norse god))",
			"as a ((egyptian god))",
			"as a ((construction worker))",
			"as a ((teacher))",
			"as a ((body builder))",
			"as a ((pirate))",
			"as a ((sanitation worker))",
			"as a ((plumber))",
			"as an ((electrician))",
			"as a ((carpenter))",
			"as a ((mechanic))",
			"as a ((farmer))",
			"as a ((fisherman))",
			"as a ((hunter))",
			"as a ((nerd))",
			"as an ((accountant))",
			"as an ((artist))",
			"as an ((athlete))",
			"as a ((baker))",
			"as a ((barber))",
			"as a ((bartender))",
			"as a ((butcher))",
			"as a ((doctor))",
			"as a ((dentist))",
			"as a ((dancer))",
			"as a ((designer))",
			"as a ((diver))",
			"as a ((director))",
			"as an ((engineer))",
			"as a ((firefighter))",
			"as a ((journalist))",
			"as a ((lawyer))",
			"as a ((mechanic))",
			"as a ((musician))",
			"as a ((nurse))",
			"as a ((pilot))",
			"as a ((police officer))",
			"as a ((salesperson))",
			"as a ((scientist))",
			"as a ((web developer))",
			"as a ((writer))",
			"as a ((warrior))",
			"as a ((mad scientist))",
			"as a ((knight in armor))",
			"as a ((jedi with a light saber))",
			"as a ((wrestler))",
			"as an ((astronaut))",
			"as a ((warlord))",
			"as a ((hobo))",
			"as a ((surfer))",
			"as a ((necromancer))",
			"as a ((thiefling))",
			"as a ((luxury person))",
			"as an ((anthropomorphic creature))",
			"as a ((samurai))",
			"as a ((viking barbarian))",
			"as an ((undead))",
			"as a ((clown))",
			"as a ((rockstar))",
			"as an ((influencer))",
			"as a ((priest))",
			"((dressed as a pope))",
			"((dressed as a king))",
			"as a ((holy person))",
			"as a ((hunter))",
			"as an ((alien being))",
			"as a ((soldier))",
			"as an ((emo))",
			"as an ((goth))",
			"as an ((video game character))",
			"as an ((michelin chef))",
			"as a ((military person))",
			"as a ((serial killer))",
			"as a ((maniac))",
			"as a ((captain))",
			"as an ((evil magician))",
			"as a ((pure blood))",
			"as a ((dragon tamer))",
			"as a ((warlock))",
			"as a ((mermaid/merman))",
			"as a ((cowboy))",
			"as a ((black metal artist))",
			"as a ((death metal front figure))",
			"as an ((alien diplomat))",
			"as a ((demigod))",
			"as a ((monster hunter))",
			"as a ((spaceship captain))",
			"((dressed as jesus))",
			"as ((the ultimate warrior))",
			"as a wall street broker yuppie",
		]

		HAIRSTYLES = [
			"with ((long hair))",
			"with ((very curly hair))",
			"with ((curly hair))",
			"with ((pixie cut hair))",
			"with ((bob cut hair))",
			"with ((undercut hair))",
			"with ((messy hair))",
			"with ((mullet hair))",
			"with ((braids))",
			"with ((french braids))",
			"with ((cornrows hair))",
			"with ((ponytail hair))",
			"with ((side part hair))",
			"with ((mohawk hair))",
			"with ((bun hair))",
			"with ((pompadour hair))",
			"with ((slicked back hair))",
			"with ((asymmetrical cut hair))",
			"with ((multicolored rainbow hair))",
			"with ((balayage hair))",
			"with ((french crop hair))",
			"with ((shaved hair))",
			"with ((shaved sides hair))",
			"with ((side swept fringe))",
			"with ((long bob haircut))",
			"with ((a-line bob haircut))",
			"with ((layered cut haircut))",
			"with ((shag cut hair))",
			"with ((buzz cut hair))",
			"with ((feathered cut hair))",
			"with ((blunt cut hair))",
			"with ((undercut hair))",
			"with ((french bob haircut))",
			"with ((textured bob haircut))",
			"with ((slicked-back haircut))",
			"with ((wedge cut haircut))",
			"with ((long layers haircut))",
			"with ((curly bob haircut))",
			"with ((cropped cut haircut))",
			"with ((faux hawk haircut))",
			"with ((angled bob haircut))",
			"with ((razor cut haircut))",
			"with ((emo haircut))",
			"with ((curtain bangs haircut))",
			"with ((waterfall braid haircut))",
			"with ((fox braids haircut))",
			"with ((chignon cut hair))",
			"with ((pigtails))",
			"with ((plait hair))",
			"with ((ponytail))",
			"with ((ringlets hair))",
			"with ((curl hair))",
			"with ((double bun topknot))",
			"with ((drill cut hair))",
			"with ((twintails hair))",
			"with ((hair set up for wedding))",
			"with ((wavy hair))",
		]

		ADDITIONAL_DETAILS = [
			"wearing a (necklace)",
			"wearing ((earrings))",
			"wearing a (bracelet)",
			"wearing one or multiple (rings)",
			"wearing a (brooch)",
			"wearing (eyeglasses)",
			"wearing (sunglasses)",
			"wearing a (hat)",
			"wearing a (scarf)",
			"wearing a (headband)",
			"wearing a (nose ring)",
			"wearing a (lip ring)",
			"wearing a (tongue ring)",
			"wearing an (eyebrow ring)",
			"wearing (face tattoos)",
			"wearing a (wreath)",
			"wearing a (crown)",
			"wearing a (tiara)",
			"wearing a (crown of thorns)",
			"wearing a (crown of jewels)",
			"wearing (bohemian clothes)",
			"wearing (chic clothes)",
			"wearing (glamorous clothes)",
			"wearing (grunge clothes)",
			"wearing (preppy clothes)",
			"wearing (punk clothes)",
			"wearing (retro clothes)",
			"wearing (rockabilly clothes)",
			"wearing (romantic clothes)",
			"wearing (tomboy clothes)",
			"wearing (urban clothes)",
			"wearing (camo clothes)",
			"wearing (robes)",
			"wearing (excessive amount of jewellery)",
			"wearing (vintage clothes)",
			"wearing (western clothes)",
			"wearing (minimalist clothes)",
			"wearing (sportswear clothes)",
			"wearing (flapper clothes)",
			"wearing (pin-up clothes)",
			"wearing (mid-century modern clothes)",
			"wearing (art deco clothes)",
			"wearing (victorian clothes)",
			"wearing (edwardian clothes)",
			"wearing (elizabethan clothes)",
			"wearing (retro 70s clothes)",
			"wearing (retro 80s clothes)",
			"wearing (retro 90s clothes)",
			"wearing (retro 00s clothes)",
			"wearing (musical equipment)",
			"wearing (leather)",
			"wearing (bdsm leather)",
			"wearing (shiny latex)",
			"wearing (shiny latex suit)",
			"wearing (silk)",
			"wearing (full tweed set)",
			"wearing (clothes made entirely of feathers)",
			"wearing (clothes made entirely of fur)",
			"wearing (clothes made entirely of leather)",
			"wearing (clothes made entirely of metal)",
			"wearing (clothes made entirely of plastic)",
			"wearing (clothes adorned with shimmering jewels or crystals)",
			"waring (clothes adorned with sequins)",
			"wearing (clothes with exaggerated or extreme silhouettes)",
			"wearing (clothes with exaggerated or extreme footwear)",
			"wearing (clothes with exaggerated or extreme headwear)",
			"wearing (clothes with exaggerated or extreme facial or body piercings or tattoos)",
			"wearing (clothes with multiple layers or tiers)",
			"wearing (clothes with exaggerated or extreme colors)",
			"wearing (clothes with exaggerated or extreme patterns)",
			"wearing (cloak)",
			"wearing an astronaut armor",
			"wearing a bio mechanical suit",
			"wearing a bio hazard suit",
			"(( working with laptop))",
			"with Heat deformation",
			"(((future soldier, full body armor, futuristic football, shoulder pads, guns, grenades, weapons, bullet proof vest, high tech, straps, belts, camouflage)))",
			"((full body, zoomed out)) long slender legs 80mm",
			"(((sci-fi, future war, cyberpunk, cyborg, future fashion, beautiful face, glowing tattoos)))",
			"((angry expression, pretty face))",
			"(((full body, athletic body, action pose, detailed black soldier outfit, slender long legs)))",
			"playing epic electric guitar solo in front of a huge crowd",
			"singing epic solo into a microphone in front of a huge crowd",
			"as a ((gelatinous horror dripping alien creature))",
		]

		# ARTWORK_STYLES = [
		# 	"digital painting",
		# 	"oil painting",
		# 	"watercolor painting",
		# 	"acrylic painting",
		# 	"pastel painting",
		# 	"charcoal drawing",
		# 	"pencil drawing",
		# 	"pen and ink drawing",
		# 	"ink drawing",
		# 	"sketch",
		# 	"line drawing",
		# 	"cartoon drawing",
		# 	"caricature drawing",
		# 	"portrait drawing",
		# 	"landscape drawing",
		# 	"still life drawing",
		# ]

		PHOTOGRAPHY_STYLES = [
			"fashion photography",
			"portrait photography",
			"landscape photography",
			"documentary photography",
			"street photography"
		]

		LENS = [
			"85mm 2.8f",
			"35mm f/1.8",
			"EF 70mm",
			"50mm f/1.2",
			"30mm f/1.4",
			"12-40mm f/2.8"
		]

		DEVICE = [
			"Hasselblad X1D-50c",
			"Nikon Z7II",
			"Canon EOS R3",
			"Sony A7R III",
			"Alexa 65",
			"Sony A7",
			"Fujifilm XT3",
			"Canon EOS R3",
			"(35mm Hasselblad 500C/M camera using Lomography colour 400 film at f/1.8)"
		]

		PHOTOGRAPHER = [
			"Alessio Albi",
			"Alvin Langdon Coburn",
			"Anne Brigman",
			"Ansel Adams",
			"Anton Corbijn",
			"Berenice Abbott",
			"Bill Brandt",
			"Brooke DiDonato",
			"Bruce Davidson",
			"Bruno Barbey",
			"Chris Burkard",
			"Claude Cahun",
			"David Bailey",
			"David Burdeny",
			"Dawoud Bey",
			"Diane Arbus",
			"Dirk Braeckman",
			"Edward Burtynsky",
			"Edward S. Curtis",
			"Elina Brotherus",
			"Elsa Bleda",
			"Erwin Blumenfeld",
			"Flora Borsi",
			"Gregory Colbert",
			"Gregory Crewdson",
			"Guy Aroch",
			"Guy Bourdin",
			"Hans Bellmer",
			"Harry Benson",
			"Harry Callahan",
			"Henri Cartier-Bresson",
			"Ilse Bing",
			"Imogen Cunningham",
			"Iwan Baan",
			"James Balog",
			"Jamie Baldridge",
			"James Balog",
			"Julia Margaret Cameron",
			"Julie Blackmon",
			"Karl Blossfeldt",
			"Katia Chausheva",
			"Keith Carter",
			"Larry Burrows",
			"Larry Clark",
			"Laurent Baheux",
			"Lewis Baltz",
			"Lillian Bassman",
			"Lynsey Addario",
			"Margaret Bourke-White",
			"Marianne Breslauer",
			"Marta Bevacqua",
			"Mathew Brady",
			"Miki Asai",
			"Miles Aldridge",
			"Nick Brandt",
			"Nobuyoshi Araki",
			"Olive Cotton",
			"Patrick Demarchelier",
			"Paul Barson",
			"Petra Collins",
			"Petra Collins",
			"Richard Avedon",
			"Rineke Dijkstra",
			"Robby Cavanaugh",
			"Robert Adams",
			"Robert Capa",
			"Roger Ballen",
			"Ruth Bernhard",
			"Slim Aarons",
			"Tami Bone",
			"Tina Barney",
			"Vanley Burke",
		]

		ARTIST = [
			"Akihito Tsukushi",
			"Al Hirschfeld",
			"Alan Lee",
			"Albert Bierstadt",
			"Albert Uderzo",
			"Alberto Giacometti",
			"Alberto Vargas",
			"Albrecht Durer",
			"Alejandro Burdisio",
			"Aleksi Briclot",
			"Alessio Albi",
			"Alena Aenami",
			"Alex Gard",
			"Alex Grey",
			"Alex Maleev",
			"Alexander Jansson",
			"Alexander Milne Calder",
			"Alexandre Cabanel",
			"Alexei Savrasov",
			"Alexej von Jawlensky",
			"Alfred Kubin",
			"Alfredo Volpi",
			"Alice Neel",
			"Alice Rahon",
			"Alphonse Mucha",
			"Alyssa Monks",
			"Amanda Clark",
			"Amanda Sage",
			"Amedeo Modigliani",
			"Amelie Bernard",
			"Anders Zorn",
			"Andreas Achenbach",
			"Andrew Wyeth",
			"Andr\u00e9 Kert\u00e9sz",
			"Andr\u00e9 Masson",
			"Andy Fairhurst",
			"Andy Singer",
			"Andy Warhol",
			"Anita Malfatti",
			"Anna Dittmann",
			"Anne Geddes",
			"Anne Stokes",
			"Anne-Louis Girodet",
			"Annibale Carracci",
			"Annie Leibovitz",
			"Ansel Adams",
			"Anthony van Dyck",
			"Anton Fadeev",
			"Anton Otto",
			"Apollonia Saintclair",
			"Arkhip Kuindzhi",
			"Arnold B\u00f6cklin",
			"Arshile Gorky",
			"Art Spiegelman",
			"Artemisia Gentileschi",
			"Arthur Dove",
			"Asaf Hanuka",
			"Asher Brown Durand",
			"Ashley Wood",
			"Audrey Kawasaki",
			"Austin Briggs",
			"Balthus",
			"Banksy",
			"Barclay Shaw",
			"Barry Blitt",
			"Bastien Lecouffe Deharme",
			"Beatrix Potter",
			"Beauford Delaney",
			"Beeple",
			"Ben Shahn",
			"Benoit B. Mandelbrot",
			"Bernard Buffet",
			"Bernd and Hilla Becher",
			"Bernie Wrightson",
			"Berthe Morisot",
			"Bill Plympton",
			"Bjarke Ingels",
			"Bob Byerley",
			"Bob Eggleton",
			"Bob Ross",
			"Boris Vallejo",
			"Brandon Woelfel",
			"Brian Despain",
			"Brian Kesinger",
			"Brothers Hildebrandt",
			"Bruce Nauman",
			"Bruce Pennington",
			"Bruno Taut",
			"Camille Claudel",
			"Camille Corot",
			"Camille Pissarro",
			"Canaletto",
			"Candido Portinari",
			"Caravaggio",
			"Carl Holsoe",
			"Carl Larsson",
			"Carne Griffiths",
			"Caspar David Friedrich",
			"Chaim Soutine",
			"Charles Blackman",
			"Charles Demuth",
			"Charles E. Burchfield",
			"Charles Eames",
			"Charles Rennie Mackintosh",
			"Chesley Bonestell",
			"Chiharu Shiota",
			"Childe Hassam",
			"Chris Foss",
			"Chris Mars",
			"Chris Menges",
			"Chris Moore",
			"Christopher Doyle",
			"Cindy Sherman",
			"Clarence Holbrook Carter",
			"Claude Cahun",
			"Claude Lorrain",
			"Claude Monet",
			"Clive Barker",
			"Clive Madgwick",
			"Clovis Trouille",
			"Clyde Caldwell",
			"Coby Whitmore",
			"Codex Seraphinianus",
			"Coles Phillips",
			"Conrad Roset",
			"Craig Mullins",
			"Cuno Amiet",
			"Dale Chihuly",
			"Damien Hirst",
			"Dan Flavin",
			"Dan Mumford",
			"Daniel Gerhartz",
			"Daniel Merriam",
			"Daniel Ridgway Knight",
			"Dave Gibbons",
			"Dave McKean",
			"David Alfaro Siqueiros",
			"David B. Mattingly",
			"David Burliuk",
			"David Hockney",
			"David Park",
			"Dean Ellis",
			"Dennis Stock",
			"Di Cavalcanti",
			"Diane Arbus",
			"Diego Velazquez",
			"Dion Beebe",
			"Don Bluth",
			"Don Maitz",
			"Donato Giancola",
			"Dora Maar",
			"Dorothea Lange",
			"Dorothea Tanning",
			"Dorothy Lathrop",
			"Doug Chiang",
			"Dustin Nguyen",
			"E.H. Shepard",
			"Earl Norem",
			"Ed Binkley",
			"Ed Emshwiller",
			"Ed Mell",
			"Edgar Degas",
			"Edmund Leighton",
			"\u00c9douard Manet",
			"Edvard Munch",
			"Edward Weston",
			"Edwin Austen Abbey",
			"Edward Hopper",
			"Egon Schiele",
			"Eikoh Hosoe",
			"El Greco",
			"Elaine de Kooning",
			"Ellen Jewett",
			"Elliott Erwitt",
			"Elsa Beskow",
			"Emil Melmoth",
			"Emil Nolde",
			"Emily Carr",
			"Emmanuel Lubezki",
			"Enki Bilal",
			"Eric Gill",
			"Eric Lacombe",
			"Erich Heckel",
			"Erich Ludwig Kirchner",
			"Ernst Fuchs",
			"Ernst Haeckel",
			"Esao Andrews",
			"Eug\u00e8ne Delacroix",
			"Eva Hesse",
			"Evelyn De Morgan",
			"Eyvind Earle",
			"Fairfield Porter",
			"Farel Dalrymple",
			"Fernand L\u00e9ger",
			"Fernando Botero",
			"Filippo Lippi",
			"Francis Bacon",
			"Francis Picabia",
			"Francisco Goya",
			"Frank Auerbach",
			"Frank Frazetta",
			"Frank Lloyd Wright",
			"Frank Miller",
			"Frank Schoonover",
			"Franklin Booth",
			"Franz Kline",
			"Franz Marc",
			"Franz Sedlacek",
			"Franz Xaver Winterhalter",
			"Fred Tomaselli",
			"Frederick Lord Leighton",
			"Frida Kahlo",
			"Friedensreich Regentag Dunkelbunt Hundertwasser",
			"Frits Van den Berghe",
			"F\u00e9lix Vallotton",
			"Gabriel Pacheco",
			"Garry Trudeau",
			"Gary Larson",
			"Gaston Bussiere",
			"Gediminas Pranckevicius",
			"Geof Darrow",
			"George Cruikshank",
			"George Frederic Watts",
			"George Grosz",
			"George Inness",
			"George Luks",
			"Georges Rouault",
			"Georges Seurat",
			"Georgia O'Keeffe",
			"Gerald Brom",
			"Gerhard Munthe",
			"Gerhard Richter",
			"Gertrude Abercrombie",
			"Giacomo Balla",
			"Giorgio de Chirico",
			"Giuseppe Arcimboldo",
			"Glenn Fabry",
			"Go Nagai",
			"Gottfried Helnwein",
			"Graciela Iturbide",
			"Grandma Moses",
			"Greg Hildebrandt",
			"Greg Rutkowski",
			"Gregory Crewdson",
			"Grzegorz Domaradzki",
			"Guido Borelli da Caluso",
			"Guillermo del Toro",
			"Gustav Klimt",
			"Gustav Vigeland",
			"Gustave Caillebotte",
			"Gustave Courbet",
			"Gustave Dore",
			"Gustave Moreau",
			"H. R. Giger",
			"Hal Foster",
			"Hannah H\u00f6ch",
			"Hans Baldung",
			"Hans Bellmer",
			"Harold Elliott",
			"Harriet Backer",
			"Harry Clarke",
			"Harry Gruyaert",
			"Heinrich Kley",
			"Hendrik Kerstens",
			"Henri Harpignies",
			"Henri Matisse",
			"Henri Rousseau",
			"Henri de Toulouse-Lautrec",
			"Henri-Edmond Cross",
			"Henry Fuseli",
			"Henry Ossawa Tanner",
			"Herg\u00e9",
			"Hieronymus Bosch",
			"Hilma af Klint",
			"Hirohiko Araki",
			"Hiromu Arakawa",
			"Hiroshi Nagai",
			"Hiroshi Yoshida",
			"Hokusai",
			"Honor\u00e9 Daumier",
			"Hope Gangloff",
			"Howard Finster",
			"Howard Hodgkin",
			"Hubert Robert",
			"Hugh Ferriss",
			"Hugh Kretschmer",
			"Hundertwasser",
			"Ian McQue",
			"Ian Miller",
			"Igor Morski",
			"Ilkka Uimonen",
			"Ilya Repin",
			"Irma Stern",
			"Isaac Levitan",
			"Isamu Noguchi",
			"Ivan Aivazovsky",
			"Ivan Albright",
			"Ivan Bilibin",
			"Ivan Generalic",
			"Ivan Shishkin",
			"J. J. Grandville",
			"J.C. Leyendecker",
			"J.M.W. Turner",
			"Jacek Yerka",
			"Jack Butler Yeats",
			"Jack Davis",
			"Jack Gaughan",
			"Jack Kirby",
			"Jackson Pollock",
			"Jacob Lawrence",
			"Jacob Riis",
			"Jacques-Laurent Agasse",
			"Jakub Rozalski",
			"James Abbott McNeill Whistler",
			"James C. Christensen",
			"James Ensor",
			"James Jean",
			"James Turrell",
			"Jamie Hewlett",
			"Jan van Goyen",
			"Jaroslaw Jasnikowski",
			"Jasmine Becket-Griffith",
			"Jason Edmiston",
			"Jason Limon",
			"Jean Arp",
			"Jean Delville",
			"Jean Giraud (Moebius)",
			"Jean Leon Gerome",
			"Jean Metzinger",
			"Jean-Auguste-Dominique Ingres",
			"Jean-Baptiste Carpeaux",
			"Jean-Baptiste-Sim\u00e9on Chardin",
			"Jean-Honore Fragonard",
			"Jean-Michel Basquiat",
			"Jean-Pierre Vasarely (Yvaral)",
			"Jeff Easley",
			"Jeff Koons",
			"Jeff Lemire",
			"Jeffrey Catherine Jones",
			"Jeffrey Smith",
			"Jeffrey T. Larson",
			"Jeremy Geddes",
			"Jeremy Lipking",
			"Jeremy Mann",
			"Jesper Ejsing",
			"Jim Burns",
			"Jim Fitzpatrick",
			"Jim Lee",
			"Jim Steranko",
			"Jithesh",
			"Joan Mir\u00f3",
			"Joaquin Sorolla",
			"Johan Christian Dahl",
			"Johannes Vermeer",
			"Johfra Bosschart",
			"John Atkinson Grimshaw",
			"John Bauer",
			"John Berkey",
			"John Blanche",
			"John Carpenter",
			"John Constable",
			"John Duncan",
			"John Frederick Kensett",
			"John Harris",
			"John Hoyland",
			"John James Audubon",
			"John Kenn Mortensen",
			"John Kricfalusi",
			"John Martin",
			"John Perceval",
			"John Philip Falter",
			"John Romita Jr",
			"John Singer Sargent",
			"John Stephens",
			"John William Waterhouse",
			"Jonas Bendiksen",
			"Josan Gonzalez",
			"Joseph Cornell",
			"Joseph Ducreux",
			"Joseph Stella",
			"Josephine Wall",
			"Jules Bastien-Lepage",
			"Jules Feiffer",
			"Jules Pascin",
			"Junji Ito",
			"Justin Gerard",
			"Kaethe Butcher",
			"Kaja Foglio",
			"Karel Thole",
			"Karl Blossfeldt",
			"Karl Schmidt-Rottluff",
			"Karol Bak",
			"Kate Greenaway",
			"Kathe Kollwitz",
			"Katsuhiro Otomo",
			"Katsushika Hokusai",
			"Kay Nielsen",
			"Kay Sage",
			"Kazimir Malevich",
			"Kehinde Wiley",
			"Kelly Freas",
			"Kelly McKernan",
			"Ken Sugimori",
			"Kenojuak Ashevak",
			"Kent Monkman",
			"Kentaro Miura",
			"Kilian Eng",
			"Kim Jung Gi",
			"Kuang Hong",
			"Larry Elmore",
			"Lasar Segall",
			"Laurel Burch",
			"Laurie Greasley",
			"Laurie Lipton",
			"Lawren Harris",
			"Le caravaggesque",
			"Lee Krasner",
			"Lee Madgwick",
			"Leiji Matsumoto",
			"Leon Bankst",
			"Leonardo da Vinci",
			"Leonid Afremov",
			"Liam Wong",
			"Liniers",
			"Lisa Frank",
			"Louis Comfort Tiffany",
			"Louis Wain",
			"Lovis Corinth",
			"Luc Schuiten",
			"Lucian Freud",
			"Luis Royo",
			"Lyonel Feininger",
			"Lyubov Popova",
			"M.C. Escher",
			"M.W. Kaluta",
			"Mab Graves",
			"Makoto Shinkai",
			"Malcolm Liepke",
			"Man Ray",
			"Marc Chagall",
			"Mark Lague",
			"Marc Simonetti",
			"Marco Mazzoni",
			"Marek Okon",
			"Margaret Boden",
			"Margaret Bruce Wells",
			"Margaret Brundage",
			"Margaret Garland",
			"Margaret Geddes",
			"Margaret Graeme Niven",
			"Margaret Keane",
			"Margaret Macdonald Mackintosh",
			"Maria Prymachenko",
			"Maria Sibylla Merian",
			"Marianne von Werefkin",
			"Mario Testino",
			"Marjorie Strider",
			"Mark Brooks",
			"Mark Catesby",
			"Mark Rothko",
			"Mark Ryden",
			"Marsden Hartley",
			"Martin Parr",
			"Martin Johnson Heade",
			"Martiros Saryan",
			"Mary Blair",
			"Mary Cassatt",
			"Masamune Shirow",
			"Masashi Kishimoto",
			"Mat Collishaw",
			"Mati Klarwein",
			"Matt Groening",
			"Matthias Grunewald",
			"Matti Suuronen",
			"Maurice Sendak",
			"Max Beckmann",
			"Max Ernst",
			"Max Pechstein",
			"Max Weber",
			"Maxfield Parrish",
			"Meret Oppenheim",
			"Michael Deforge",
			"Michael Whelan",
			"Michelangelo",
			"Mike Mignola",
			"Mikhail Vrubel",
			"Miles Aldridge",
			"Milton Avery",
			"Milton Glaser",
			"Moebius (Jean Giraud)",
			"Mort Drucker",
			"Nan Goldin",
			"Nao Emoto",
			"Naoto Hattori",
			"Natalia Goncharova",
			"Neil Welliver",
			"Nele Zirnite",
			"Nell Dorr",
			"Nicholas Roerich",
			"Nick Knight",
			"Nikos Economopoulos",
			"Nobuyoshi Araki",
			"Noriyoshi Ohrai",
			"Norman Rockwell",
			"Nychos",
			"Odd Nerdrum",
			"Odilon Redon",
			"Oliver Jeffers",
			"Oskar Kokoschka",
			"Oskar Schlemmer",
			"Otto Dix",
			"Otto Marseus van Schrieck",
			"Pablo Picasso",
			"Pascal Campion",
			"Patrick Henry Bruce",
			"Patrick Heron",
			"Patrick Nagel",
			"Patrick Woodroffe",
			"Paul Cezanne",
			"Paul Delvaux",
			"Paul Gauguin",
			"Paul Gustav Fischer",
			"Paul Klee",
			"Paul Rand",
			"Paula Modersohn-Becker",
			"Pendleton Ward",
			"Peter Bagge",
			"Peter Elson",
			"Peter Gric",
			"Peter Kemp",
			"Peter Max",
			"Peter Paul Rubens",
			"Phil Foglio",
			"Philip Guston",
			"Philip Pearlstein",
			"Philip-Lorca diCorcia",
			"Pierre Bonnard",
			"Pierre-Auguste Renoir",
			"Piet Mondrian",
			"Pieter Claesz",
			"Platon",
			"Quentin Blake",
			"Rachel Ignotofsky",
			"Rafal Olbinski",
			"Ralph McQuarrie",
			"Ralph Steadman",
			"Ram\u00f3n Casas",
			"Randolph Caldecott",
			"Raphael Lacoste",
			"Raphaelite",
			"Ray Caesar",
			"Ray Earnes",
			"Raymond Briggs",
			"Raymond Swanland",
			"Rebeca Saray",
			"Rebecca Guay",
			"Reginald Marsh",
			"Remedios Varo",
			"Ren\u00e9 Magritte",
			"Richard Corben",
			"Richard Dadd",
			"Richard Diebenkorn",
			"Richard Doyle",
			"Richard Scarry",
			"Ridley Scott",
			"Rineke Dijkstra",
			"Rob Gonsalves",
			"Rob Liefeld",
			"Robert Bechtle",
			"Robert Capa",
			"Robert Crumb",
			"Robert Delaunay",
			"Robert McCall",
			"Robert McGinnis",
			"Robert Motherwell",
			"Robert Rauschenberg",
			"Robert Williams",
			"Roberto Ferri",
			"Roberto Matta",
			"Rockwell Kent",
			"Rodney Matthews",
			"Rodrigo Prieto",
			"Roger Dean",
			"Romare Bearden",
			"Romero Britto",
			"Ron Walotsky",
			"Rosa Bonheur",
			"Roy Lichtenstein",
			"Rudolf Hausner",
			"Rufino Tamayo",
			"Russ Mills",
			"Ruth Bernhard",
			"Ryan Hewett",
			"Ryo Takemasa",
			"Ryohei Hase",
			"Sally Mann",
			"Salvador Dali",
			"Sam Bosma",
			"Sam Francis",
			"Sam Guay",
			"Sam Toft",
			"Santiago Caruso",
			"Satoshi Kon",
			"Sebastian Kr\u00fcger",
			"Sebasti\u00e3o Salgado",
			"Sergio Toppi",
			"Shaun Tan",
			"Shepard Fairey",
			"Shiki",
			"Shinji Aramaki",
			"Shotaro Ishinomori",
			"Sidney Nolan",
			"Sidney Prior Hall",
			"Simon Bisley",
			"Simon St\u00e5lenhag",
			"Simone Martini",
			"Sir James Guthrie",
			"Sir Max Beerbohm",
			"Sonia Delaunay",
			"Stanley Donwood",
			"Stefan Gesell",
			"Stephanie Law",
			"Stephen Gammell",
			"Steve Argyle",
			"Steve Dillon",
			"Steve Ditko",
			"Steve McCurry",
			"Storm Thorgerson",
			"Stuart Davis",
			"Syd Mead",
			"Sylvain Chomet",
			"Taiyo Matsumoto",
			"Takashi Murakami",
			"Takato Yamamoto",
			"Takehiko Inoue",
			"Taro Okamoto",
			"Tarsila do Amaral",
			"Tatsuro Kiuchi",
			"Ted Nasmith",
			"Terry Oakes",
			"Tex Avery",
			"Theodor Seuss Geisel",
			"Thomas Cole",
			"Thomas Gainsborough",
			"Thomas Kinkade",
			"Tibor Nagy",
			"Tillie Walden",
			"Tim Burton",
			"Tim Doyle",
			"Tim Hildebrandt",
			"Tim White",
			"Tivadar Csontvary Kosztka",
			"Todd McFarlane",
			"Tom Bagshaw",
			"Tom Lovell",
			"Tom Thomson",
			"Tom Whalen",
			"Tomasz Alen Kopera",
			"Tomasz Jedruszek",
			"Tomek Setowski",
			"Tomer Hanuka",
			"Tomi Ungerer",
			"Tomioka Tessai",
			"Tommaso Dolabella",
			"Tommaso Masaccio",
			"Tommaso Redi",
			"Tomokazu Matsuyama",
			"Tom\u00e0s Barcel\u00f3",
			"Tony DiTerlizzi",
			"Tove Jansson",
			"Tsutomu Nihei",
			"Ub Iwerks",
			"Van Herpen",
			"Victo Ngai",
			"Victor Brauner",
			"Victor Moscoso",
			"Victor Ngai",
			"Victor Vasarely",
			"Viktor Vasnetsov",
			"Vilhelm Hammershoi",
			"Vilmos Zsigmond",
			"Vincent van Gogh",
			"Virgil Finlay",
			"Walter Crane",
			"Walt Disney",
			"Wassily Kandinsky",
			"Wayne Barlowe",
			"Weegee",
			"Wes Anderson",
			"Will Simpson",
			"Wifredo Lam",
			"William Blake",
			"William Gropper",
			"William Henry Hunt",
			"William Hogarth",
			"William Morris",
			"William S Burroughs",
			"William Stout",
			"William-Adolphe Bouguereau",
			"Winslow Homer",
			"Wong Kar-Wai",
			"Yaacov Agam",
			"Yayoi Kusama",
			"Yoshitaka Amano",
			"Yousuf Karsh",
			"Yuumei",
			"Yves Klein",
			"Yves Tanguy",
			"Zack Snyder",
			"Zaha Hadid",
			"Zdzislaw Beksinski",
		]

		DIGITAL_ARTFORM = [
			"Vector Art",
			"Digital Painting",
			"Glitch Art",
			"Digital Collage",
			"Digital art",
			"Digital illustration",
			"Concept art",
			"Digital water color painting",
			"Digital drawing",
			"digital painting",
			"oil painting",
			"watercolor painting",
			"acrylic painting",
			"pastel painting",
			"charcoal drawing",
			"pencil drawing",
			"pen and ink drawing",
			"ink drawing",
			"sketch",
			"line drawing",
			"cartoon drawing",
			"caricature drawing",
			"portrait drawing",
			"landscape drawing",
			"still life drawing",
		]

		PLACE = [
			"indoor",
			"outdoor",
			"at night",
			"in the park",
			"studio",
			"at a party",
			"at a festival",
			"at a concert",
			"on persons home planet",
			"magical portal with particles",
			"in a neon lit city",
			"in a cyberpunk city",
			"in a fantasy world",
			"glamour photography",
			"fashion photography",
			"at home",
			"at work",
			"at a cafe",
			"at a gym",
			"at a hotel",
			"at a concert performance",
			"at the beach",
			"at a museum",
			"in a hidden city deep in the rainforest",
			"in a floating island in the sky",
			"in an underground world beneath the earths surface ",
			"in a secret garden hidden in a mysterious maze",
			"in a grand castle on the top of a remote mountain",
			"in a enchanted forest with talking animals and magical creatures",
			"in a mystical island filled with ancient ruins and hidden treasure",
			"in a faraway planet with a unique and alien landscape",
			"in a hidden paradise hidden behind a waterfall",
			"in a dreamlike world where anything is possible and the impossible is real",
			"in a hidden oasis in the desert",
			"in a secret underground city",
			"in an underwater kingdom",
			"in a lost temple in the jungle",
			"in a castle in the clouds",
			"in a hidden valley in the mountains",
			"in a uturistic city on a distant planet",
			"in a mystical land of eternal twilight",
			"Smoke and ash in the air",
		]
		LIGHTING = [
			"bokeh",
			"dramatic",
			"golden hour",
			"depth of field",
			"movie still",
			"colorful",
			"soft lighting",
			"studio lighting with strong rim light",
			"ambient lighting",
			"sun rays",
			"cinematic lighting",
			"characteristics of the light",
			"volumetric lighting",
			"natural point rose",
			"outdoor lighting",
			"soft pastel lighting colors scheme",
			"sensual lighting",
			"neon lights",
			"baroque",
			"rokoko",
			"rim light, iridescent accents",
			"neoclassicism",
			"realism",
			"fantastic colors",
			"surrealism",
			"futurism",
			"accent lighting",
			"high key lighting",
			"low key lighting",
			"strong backlight",
			"artificial lighting",
			"decorative lighting",
			"recessed lighting",
			"wall sconces lighting",
			"laser lighting",
			"multi-colored lighting",
			"mood lighting",
			"accent lighting",
			"projection lighting",
			"bioluminiscent",
			"plasma",
			"ice",
			"water",
			"rule of thirds",
			"anamorphic lens flare",
			"sharp focus",
			"vivid colors",
			"masterpiece",
			"colors",
			"8k",
			"atmospheric",
			"cinematic sensual",
			"hyperrealistic",
			"big depth of field",
			"glow effect",
			"modelshoot style",
			"shallow depth of field",
			"hdr",
			"dynamic composition",
			"broad light",
			"natural lighting",
			"elegant pose",
			"flowing",
			"film photo",
			"extremely detailed",
			"big depth of field",
			"matte skin, pores, wrinkles",
			"hyperdetailed",
			"(abstract:1.3)",
			"intricate and low contrast detailed",
			"(composition)",
			"film grain",
			"(8k, RAW photo, best quality, masterpiece:1.2)",
			"(realistic, photo-realistic:1.37)",
			"beautiful detailed eyes, beautiful detailed lips, a captivating gaze, and an alluring expression",
			"beautiful dynamic dramatic dark moody lighting",
			"(detailed face:1.3)",
			"multilayered realism",
			"majestically strides forward toward us with abandon",
			"disintegrating moon",
			"extremely intricate details",
			"anatomical beauty",
			"high fantasy",
			"detailed skin pores",
			"flat color scheme",
			"80s music clip background",
			"Use a backlighting effect to add depth to the image. impressionistic painting style, john singer sarget, blue pallette",
			"(natural skin texture, hyperrealism, soft light, sharp:1.2)",
			"(cinematic, teal and orange:0.85)",
			"(intricate skin detail:1.3), (wrinkles:1.2),(skin blemishes:1.1),(skin pores:1.1),(detailed face:1.3), (lips slightly parted:1.0)",
			"(muted colors, dim colors, soothing tones:1.3), low saturation, (hyperdetailed:1.2)",
			"(noir:0.4), (intricate details:1.12), hdr, (intricate details, hyperdetailed:1.15)",
			"(neutral colors:1.2), art, (hdr:1.5), (muted colors:1.1), (pastel:0.2), hyperdetailed",
			"dramatic lighting",
			"((landscape view)), 4k unity, (best illumination)",
			"dynamic angle",
			"detailed freckles skin",
			"movie grain",
			"epic composition",
			"Tarot Card style",
			"(solo focus, one frame)",
			"(masterpiece, best quality, ultra-detailed, highres)",
			"biopunk",
			"dramatic Pull from the ghost of a virtual memory",
			"gritty industrial",
			"(soothing tones, insane details, intricate details, hyperdetailed,photorealistic,dim subdued lighting)",
		]
		is_photographer = random.choice([True, False])
		prompt = f"{random.choice(INITIAL_DESCRIPTION)} of a {random.choice(EMOTIONS)} "
		selected_lighting = random.sample(LIGHTING, random.randint(2, 5))
		comma_separated_lighting = ", ".join(selected_lighting)		
        # Use the input tag or a default tag if the input is empty
		if subject:
			prompt += f"{subject} "
		else:
			prompt += f"{random.choice(DEFAULT_TAGS)} "
        
		prompt += f"{random.choice(ROLES)} {random.choice(HAIRSTYLES)} {random.choice(ADDITIONAL_DETAILS)}, {random.choice(PLACE)}, {comma_separated_lighting} "
        
		if is_photographer:
			prompt += f", {random.choice(PHOTOGRAPHY_STYLES)}, {random.choice(LENS)} shot on {random.choice(DEVICE)} photo by {random.choice(PHOTOGRAPHER)}"
		else:
			prompt += f", {random.choice(DIGITAL_ARTFORM)} by {random.choice(ARTIST)}"
		
		print(f"AUTOPROMPT: {prompt}")
		return (prompt,)

NODE_CLASS_MAPPINGS = {
    "PromptGenerator": PromptGenerator,
}

# Human readable names for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptGenerator": "SDXL Auto Prompter",
}
