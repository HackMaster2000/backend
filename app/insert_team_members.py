from app.models import TeamMember
from app.team_members import teamMembers

def insertTeamMembers():
    for teamMember in teamMembers:
        t = TeamMember(
            first_name=teamMember['first_name'],
            last_name=teamMember['last_name'],
            position=teamMember['position'],
            bio=teamMember['bio'],
            image=teamMember['image'],
        )
        t.save()