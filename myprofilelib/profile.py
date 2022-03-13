from pickle import NONE, TRUE

class MyFortFolio:
	def __init__(self, FirstName, LastName):
		self.firstname = FirstName
		self.lastname = LastName
		self.picture = ''
		self.greeting = ''
		self.coverimage = ''
		self.flash_greeting_header = ''
		self.flash_greeting = ''
		self.highlighted_skills =[]
		self.contactinfo = []
		self.links = []
		self.aboutme = NONE
		self.services = []
		self.awards = []
		self.portfolio = []
		self.educations = []
		self.experience = []
		self.skills = []
		self.skill_image = ''
		self.resume_image = ''
		self.resume_header = ''
		self.resume_desc = ''
		self.resume_link = ''
		self.postscript = ''
		self.footer = ''

class SkillLink:
	def __init__(self,title, link):
		self.title = title
		self.link = link

class ContactInfo:
	def __init__(self, detail, icon):
		self.detail = detail
		self.icon = icon

class UrlLinks:	
	def __init__(self, link, icon):
		self.link = link
		self.icon = icon	

class AboutMe:
	def __init__(self, aboutme, sidepic, qoute, author, source):
		self.aboutme = aboutme
		self.sidepic = sidepic
		self.qoute = qoute
		self.author = author
		self.source = source

class Serivce:
	def __init__(self, title, description, image):
		self.title = title
		self.description = description
		self.image = image

class Awards:
	def __init__(self, title, image, description):
		self.title = title
		self.image = image
		self.description = description

class Works:
	def __init__(self, image, title, description, link):
		self.image = image
		self.title = title
		self.description = description
		self.link = link

class Education:
	def __init__(self, level, years, school, course):
		self.level = level
		self.years = years
		self.school = school
		self.course = course

class Experience:
	def	__init__(self, position, duration, company, present):
		self.position = position
		self.duration = duration
		self.company = company
		self.present = present 		

class Skill:
	def __init__(self, language, description, years, percentage):
		self.language = language
		self.description = description
		self.years = years
		self.percentage = percentage	
	
class Resume:
    def	__init__(self) -> None:
        self.header = ''
        self.description = ''
        self.sampleimage = ''

def getInitializeProfile():
    myprofile = MyFortFolio('Ralph Anthony', 'de Luna')
    myprofile.firstname = 'Ralph Anthony'
    myprofile.lastname = 'de Luna'
    myprofile.coverimage = 'images/coverBG.png'
    myprofile.picture = 'images/MyPhoto2.png'
    myprofile.greeting = "Hi! I'm"
    myprofile.flash_greeting_header = "Hello There!"
    myprofile.flash_greeting = "I'm Ralph. Thank you for checking my portfolio."
    myprofile.skill_image = 'images/Wallpaper.png'
    myprofile.resume_image = 'images/myResume.png'
    myprofile.resume_header = 'Download my resume.'
    myprofile.resume_desc = 'If you are interested in my other information.you can click the button below.'
    myprofile.resume_link = 'files/Resume - Ralph Anthony A. de Luna 2022.pdf'
    myprofile.postscript = 'Hoping you got what you came for.'
    myprofile.footer = '2022 My Portfolio'

    myprofile.highlighted_skills.append(SkillLink("Winforms C#","https://en.wikipedia.org/wiki/Windows_Forms"))
    myprofile.highlighted_skills.append(SkillLink("Android Java","https://en.wikipedia.org/wiki/Android_software_development"))
    myprofile.highlighted_skills.append(SkillLink("SQL DB Admin","https://en.wikipedia.org/wiki/Database_administrator"))
    myprofile.highlighted_skills.append(SkillLink("IoT Developer","https://en.wikipedia.org/wiki/Internet_of_things"))

    myprofile.contactinfo.append(ContactInfo('+63915 259 3599','fa fa-phone'))
    myprofile.contactinfo.append(ContactInfo('dev1506ralphanthony','fa fa-skype'))
    myprofile.contactinfo.append(ContactInfo('ralph.deluna.rtatzs@gmail.com','fa fa-envelope'))

    myprofile.links.append(UrlLinks('https://linkedin.com/in/ralph-anthony-de-luna-73a91a16a/','fa fa-linkedin-square'))
    myprofile.links.append(UrlLinks('https://web.facebook.com/Rtatzs/','fa fa-facebook-square'))
    myprofile.links.append(UrlLinks('https://www.instagram.com/ralphtatzs/','fa fa-instagram'))
    myprofile.links.append(UrlLinks('https://github.com/rtatzs/','fa fa-github'))

    myprofile.aboutme = AboutMe("I spent five years maintaining a Quality Assurance System of an ISO-certified client that produces electronics for Aviation. I am well acquainted with the manufacturing environment from onsite deployments. My recent work involves the development of software for the Internet of Things (IoT) which includes reading data from sensors and controlling field devices. I am eager to learn and can work with less supervision. You can expect me to have initiative.",
                                "images/Mountain.png",
                                "It is always cheaper to do the job right the first time.",
                                "Phil Crosby",
                                "Zero Defects Program")

    myprofile.services.append(Serivce("5 Major Projects","Having crucial role involving planning, system design, development, implementation, quality assurance, deployment and maintenance of projects.","images/work-in-progress.png"))
    myprofile.services.append(Serivce("2 Yrs in Research","Spent two years designing and developing softwares for IoT and connection to PLC. This includes negotiating hardware supplier locally and overseas.","images/investigation.png"))
    myprofile.services.append(Serivce("10,800 Hrs CRM","Has five years experience handling customer relation through call, email and onsite deployments.","images/handshake.png"))
    myprofile.services.append(Serivce("2 Yrs Supervisory","Has experience in handling employees and performing management related tasks. This includes scheduling projects and monitoring maintenance hours.","images/strategy.png"))
    myprofile.services.append(Serivce("Active Participant","Active participation to company actvities including outing and community extension services.","images/plant.png"))

    myprofile.awards.append(Awards("Deployment Award  2016","images/2016.png","Recognition for exemplary performance in the ERP Project - Quality Assurance System Enhancement."))
    myprofile.awards.append(Awards("Pedestal Award 2018","images/2018.png","Recognition for exemplary performance for year 2018."))
    myprofile.awards.append(Awards("Service Award 2020","images/2020.png","Recognition for the invaluable service, dedication and loyalty rendered to the company."))
    myprofile.awards.append(Awards("Pedestal Award 2021","images/2021.png","For closing a JAE AUTO-PCR Stamping Development and Implementation and Android Application Development sold and deployed to Medilinx."))

    myprofile.portfolio.append(Works("images/Winforms.jpg","C# Winfoms","Maintenance of winform application that reads data directly from a measuring microsccope. The system is for Quality Assurance.",""))
    myprofile.portfolio.append(Works("images/SQL Server.jpg","SQL Server","Design, Maintenance and Optimization of SQL Database.",""))	
    myprofile.portfolio.append(Works("images/Android.png","Android Java Developer","Developed a mobile app for scanning of items withdrawn from warehouse and sending data to cloud server.",""))
    myprofile.portfolio.append(Works("images/noderead.png","IoT with Node JS & Python","Development of Linkage to IoT software providers with creators basing from Japan.",""))
    myprofile.portfolio.append(Works("images/Modbus.png","Internet of Things","Development and client demonstration of IoT application to manufacturing (proof of concent). This Includes wiring sensor and connection to field devices via Modbus RTU RS485. I developed a REST API to access field devices data with less to none plc programming.","https://youtu.be/twWxX3Yu1wM"))
    myprofile.portfolio.append(Works("images/Flask.png","Flask Application","This Portfolio website is created using flask in Python. Source code is public and available in my github.","https://github.com/rtatzs/My-Portfolio"))
	

    myprofile.educations.append(Education("College","2010 - 2015","University of Scan Carlos","Bacheclor of Science in Computer Science"))
    myprofile.educations.append(Education("High School","2006 - 2010","Mandaue City Comprehensive National High School",""))
    myprofile.educations.append(Education("Primary School","2000 - 2006","Mandaue City Central School",""))

    myprofile.experience.append(Experience("Supervisor","Jan 2020 - Present","N-PAX Cebu Corporation",'TRUE'))
    myprofile.experience.append(Experience("Senior Programmer","Jan 2018 - Dec 2019","N-PAX Cebu Corporation",""))
    myprofile.experience.append(Experience("Programmer","Nov 2015 - Jan 2018","N-PAX Cebu Corporation",""))
    myprofile.experience.append(Experience("Intern","Nov 2015 - Jun 2016","N-PAX Cebu Corporation",""))

    myprofile.skills.append(Skill("Winform C#","Development","5","90"))
    myprofile.skills.append(Skill("SQL Server","Design and Database Administration","5","90"))
    myprofile.skills.append(Skill("Android Java","Development","1.5","60"))
    myprofile.skills.append(Skill("Python","Project Development","1.5","50"))
    myprofile.skills.append(Skill("Node JS","Project Development","1.5","50"))
    myprofile.skills.append(Skill("Arduino","Project Development","1.5","50"))
    myprofile.skills.append(Skill("Keyence PLC","Design and Development","1.5","50"))
    
    return myprofile