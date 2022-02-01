import discord
from discord.ext import commands
from datetime import datetime

bot = commands.Bot(command_prefix='.')

# assignment name, [due date, # of points assignment is worth]
hw      =   {  'LAB1'   : ['01-20-2022 23:59:59',  10],
               'LAB2'   : ['02-01-2022 23:59:59',  30],
               'LAB3'   : ['02-01-2022 23:59:59',  30] } 

exams  =    {  'EXAM1'   : ['01-21-2022 23:59:59',  100],
               'EXAM2'   : ['01-29-2022 23:59:59',  100],
               'EXAM3'   : ['01-23-2022 23:59:59',  100] } 

quizzes  =  {  'QUIZ1'   : ['01-21-2022 23:59:59',  20],
               'QUIZ2'   : ['01-29-2022 23:59:59',  20],
               'QUIZ3'   : ['01-29-2022 23:59:59',  20] } 


def get_assignment_type(assignment_type):
    """
    Gets the assignment type (the name of the dictionary)
    """
    keys = list(assignment_type.keys())
    key_name = keys[0]
    result = ''.join([i for i in key_name if not i.isdigit()])
    return(result)

def next_due_date(assignment_type):
    """
    Gets the due date of the assignment type (hw, exams or quizzes)
    """
    now = datetime.now()
    for key, values in assignment_type.items():
        due_date = datetime.strptime(values[0],'%m-%d-%Y %H:%M:%S')
        if due_date < now:
            continue
        else:
            break
    
    return due_date
    
def search(date, assignment_type):
    """
    searches for assignments that are due
    """
    new_list = []
    
    for keys, values in assignment_type.items():
        due_date = datetime.strptime(values[0],'%m-%d-%Y %H:%M:%S')
        if(due_date == date):
            new_list.append(keys)
    
    return new_list

def current_assignment(assignment_type):
    """
    gets the current due date, and searches for assignments that are due
    """
    due_date = next_due_date(assignment_type)
    print(due_date)
    assignment_list = search(due_date, assignment_type)
    return assignment_list

def how_many_left(assignment_type):
    """
    counts how many assignments are left in the semester.
    gets the current time, and compares the time to the assignment's due date.
    increments counter if due date hasn't passed
    """
    count = 0
    now = datetime.now()
    due_date = next_due_date(assignment_type)
    
    for  keys, values in assignment_type.items():
        due_date = datetime.strptime(values[0],'%m-%d-%Y %H:%M:%S')
        if due_date < now:
            continue
        else:
            count += 1

    name = get_assignment_type(assignment_type)
    new_list = [name, count]

    return new_list


def late_penalty(assignment_name):
    """
    calculates how many days an assignment is late,
    and applies late penalties to the assignment
    """
    now = datetime.now()
    print(now)
    if assignment_name in hw:
        due_date = datetime.strptime(hw[assignment_name][0],'%m-%d-%Y %H:%M:%S')
        assignment_points = hw[assignment_name][1]

    elif assignment_name in exams:
        due_date = datetime.strptime(exams[assignment_name][0],'%m-%d-%Y %H:%M:%S') 
        assignment_points = exams[assignment_name][1]

    else:
        print("no assignment with that name!")
        return
        
    days_late = (now - due_date).days
    
    if days_late <= 0:
        new_list = [0, assignment_points]
        return new_list
    elif days_late == 1:
        assignment_points = assignment_points - (assignment_points * .10)
    elif days_late == 2:
        assignment_points = assignment_points - (assignment_points * .20)
    elif days_late == 3:
        assignment_points = assignment_points - (assignment_points * .30)
    elif days_late == 4:
        assignment_points = assignment_points - (assignment_points * .40)
    elif days_late == 5:
        assignment_points = assignment_points - (assignment_points * .50)
    else:
        assignment_points = 0

    new_list = [days_late, assignment_points]
    return new_list


@bot.command()
async def comm_info(ctx):
    long_string = (
    'teacheremail@test.edu - does not respond on weekends\n'
    'lab_instructoremail@test.edu - does not respond on weekends'
)
    await ctx.reply(long_string)

@bot.command()
async def office_hours(ctx):
    now = datetime.now().isoweekday()
    if now == 1:
        s = "today is monday\noffice hours for monday: 12:00PM - 1:00PM"    
    elif now == 2:
        s = "today is tuesday\nthere are no office hours today"
    elif now == 3:
        s = "today is wednesday\noffice hours for wednesday: 11:00AM - 12:00PM"
    elif now == 4:
        s = "today is thursday\nthere are no office hours today"    
    elif now == 5:
        s = "today is friday\noffice hours for friday: 11:00AM - 12:00PM"  
    else:
        s = "it is the weekend. there are no office hours scheduled on weekends."
    
    await ctx.reply(s)

@bot.command()
async def current_assignments(ctx, assignment_type):
    if assignment_type == 'hw':
         await ctx.reply("current hw assignments: {0}".format(current_assignment(hw)))
    elif assignment_type == 'exams':
         await ctx.reply("next exam {0}".format(current_assignment(exams)))
    elif assignment_type == 'quizzes':
        await ctx.reply("next exam {0}".format(current_assignment(exams)))
    else:
        await ctx.reply("This assignment type does not exist")

        
@bot.command()
async def hw_details(ctx, assignment):
    hw_det = hw[assignment]
    s = "{0} is due on {1} and is worth {2} percent of your grade.".format(assignment, hw_det[0], hw_det[1])
    await ctx.reply(s)

@bot.command()
async def exam_details(ctx, assignment):
    exam_det = exams[assignment]
    s = "{0} is due on {1} and is worth {2} percent of your grade.".format(assignment, exam_det[0], exam_det[1])
    await ctx.reply(s)

@bot.command()
async def quiz_details(ctx, assignment):
    quiz_det = hw[assignment]
    s = "{0} is due on {1} and is worth {2} percent of your grade.".format(assignment, quiz_det[0], quiz_det[1])
    await ctx.reply(s)

@bot.command()
async def how_many(ctx, assignment_type):
    if assignment_type == 'hw':
        new_list = how_many_left(hw)
    elif assignment_type == 'exams':
        new_list = how_many_left(exams)
    elif assignment_type == 'quizzes':
        new_list = how_many_left(quizzes)
    else:
        s = "This assignment type does not exist"
        await ctx.reply(s)

    s = "assignment Type: {0}\nnumber remaining: {1}".format(new_list[0], new_list[1])
    await ctx.reply(s)

@bot.command()
async def late(ctx, assignment_name):
    new_list = late_penalty(assignment_name)
    s = "{0} is {1} day(s) late\nmaximum points earnable: {2}".format(assignment_name, new_list[0], new_list[1])
    await ctx.reply(s)

@bot.command()
async def book_links(ctx):
    s = "www.link-to-book.com\nalso purchasable @ amazon.com/link_to_book"
    await ctx.reply(s)

bot.run('OTM2ODE1OTMxNTEyOTg3NzE5.YfSr0w.dMBWIOFDokK0Mxe5MIHIFtePZUo')
