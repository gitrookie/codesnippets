from launchpadlib.launchpad import Launchpad

lp = Launchpad.login_with(
        'test', 'https://api.launchpad.net/', version='devel')
print(lp.bugs.lp_entries)
project = lp.projects['hplip']
print(project)
sim_questions = project.findSimilarQuestions(phrase="1018")
# print(dir(sim_questions))
# print(len(sim_questions))

for ques in sim_questions:
    print(ques.date_created)
    break
