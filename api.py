from re import M
from classes import Result
from flask import Flask, render_template, request, redirect, url_for,session,flash

from difflib import SequenceMatcher

app = Flask(__name__)
app.config["DEBUG"] = True

def init():
    mp = {}
    mp["What are the terms and conditions of the scholarships?"] = """
    Information on SUTD-administered scholarships can be found here. In your online application for admission, simply check the box in the section on Scholarships to indicate your interest to apply. If you have financial need, you may wish to improve your chances of securing a scholarship with a higher quantum of support by separately applying for financial aid (those enrolling in the immediate year will receive an email invite to apply for financial support upon receiving the admission offer notification).
 
Students who demonstrate academic excellence, leadership qualities, special talents, good moral character and strong community spirit, could be recognised and rewarded with distinguished scholarships awarded by SUTD, generous donors and sponsor corporations.
 
Do note that these scholarships are limited in numbers and are awarded on the basis of competition among eligible applicants. For International Students, scholarships generally cover up to the tuition fees for a Singapore Citizen.
    """
    mp["What are the terms and conditions of the scholarships?"] = '''The terms and conditions of the various SUTD-administered scholarships are available on the respective scholarship pages.

Scholarship recipients will also receive the scholarship agreement which details the terms and conditions when school term starts.'''
    mp["How can I apply for a scholarship if I am not offered one at admission?"] = '''Students will receive email notifications whenever there are SUTD-administered mid-term scholarships open for application. You can submit an application if you meet the stipulated criteria.

Do note that these scholarships are limited in numbers and are awarded on the basis of competition among eligible applicants. For International Students, scholarships generally cover up to the tuition fees for a Singapore Citizen unless specified otherwise.

Alternatively, you may consider applying for external scholarships.'''
    mp["How do I apply for financial aid at SUTD?"] = '''Incoming Students: via Admissions Portal
Existing Students: via MyPortal

More information on financial aid can be found here.'''
    mp["When can I start applying for financial aid?"] = '''Incoming Students:
For students admitting in the impending intake, application for financial aid may be made upon receiving the admission offer notification. Students who have a place reserved for future intakes may apply for financial aid in the year of your matriculation.
 
Existing Students:
The main financial aid application cycle is usually held at the start of the year. Students will be notified on the application window via email.

All students will be assessed on your eligibility for Government Bursaries, SUTD Education Opportunity Grant (SEOG)* and/or SUTD-administered Study/Bursary Awards/Special Programme/Grants.
 
*The grant from the SEOG may comprise donor-supported EOGs and/or donor bursary awards. Funding for hostel fees is only applicable for the Freshmore terms where hostel stay is compulsory.''' 
    mp["What should I do if I missed the main financial aid application?"] = '''The main financial aid application cycle takes place once a year. However, there are also ad-hoc application cycles for the Government Bursaries. Students will be notified on the application windows via email.

Eligible applicants are entitled to receive Government Bursaries only once in each academic year. Reapplication is required every year.

Students who have been awarded Government Bursaries under the main application cycle do not have to re-apply during the ad-hoc application cycles for the Government Bursaries within the same calendar year.'''

    mp["When will I know the results for my financial aid application made during Admission?"] = '''You will receive an email on the interim financial aid offer upon the submission of your financial aid application. 

Please note that the award(s) stated in the interim offer is/are subject to change after assessment of your financial need.

If you are unsuccessful in the application, you may apply again in the following year.'''

    mp["Is there financial aid for International Students?"] = '''Financial aid for International Students are very limited. International Students may apply for Tuition Fee Loan and Study Loan to help defray your tuition fees. It is important to note that the loan amount is capped at the tuition fees for a Singapore Citizen.
 
Outstanding International Students who have applied for SUTD scholarships may also be awarded a scholarship along with your admission offer.
 
Students should fully consider your financial options before deciding whether to accept the admission offer'''

    return mp

def similarirty(a, b):
    return SequenceMatcher(None, a, b).ratio()

def getResults(keyword):
    res = []
    
    for key, value in dummyData.items():
        s = similarirty(key, keyword)
        if keyword in key and s > 0:
            res.append((s, Result(key, value, round(s, 2) * 100)))
    print(sorted(res, key = lambda x: -x[0]))
    return [item[1] for item in sorted(res, key = lambda x: -x[0])]
            
            

dummyData = init()
print(dummyData.keys())

@app.route('/', methods=['GET'])  #homepage
def home():
    return render_template("index.html")

@app.route('/results', methods=['POST'])  #homepage
def results():
    res = getResults(request.form["item"])
    
    return render_template("results.html", res = res)
            
if __name__ == "__main__":
    app.run()
