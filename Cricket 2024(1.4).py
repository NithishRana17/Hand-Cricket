def inn(choice,r,bb):
    import random
    print()
    if choice == r:
        print('You won the Toss!!')
        In = input('Bat/Bowl: ').lower()
        if In.upper() not in bb:
            print('Enter Correct Choice')
            return inn(choice,r,bb)
        print('You choose to', In)
        return In.upper()
    else:
        print('PC won the Toss!!')
        In = random.choice(bb)
        print('PC choose to', In)
        if In == 'BAT':
            In = 'BOWL'
        else:
            In = 'BAT'
        return In
def toss():
    import random
    print()
    tos = ['H','T']
    bb = ['BAT', 'BOWL']
    choice = input('Call (H/T): ').upper()
    if choice.upper() not in tos:
        print('Enter Correct Choice')
        return toss()
    r = random.choice(tos)
    Inn = inn(choice, r, bb)
    return Inn
def bat_card(players,p_runs,p_out,p_balls):
    print()
    print('--BATTING CARD--')
    for i in range(len(players)):
        if p_out[i] == 1:
            print(players[i], end = ' - ')
            print(p_runs[i],'* ','(',p_balls[i],')', sep = '')
        elif p_out[i] == 2:
            print(players[i], end = ' - ')
            print(p_runs[i],' (',p_balls[i],')', sep = '')
    print()
def bowl_card(players,p_wickets,p_overs,p_rpo):
    print()
    print('--BOWLING CARD--')
    for i in range(len(players)):
        if p_overs[i] > 0:
            print(players[i])
            print('  ',round(p_overs[i]),'O ',p_rpo[i],'R ',p_wickets[i],'W ')
    print()
def ov():
    try:
        print()
        ovr = int(input('Enter overs per innings: '))
        return ovr
    except ValueError:
        print('Enter Only  Non- Zero Integer Value')
        return ov()
def p_c():
    try:
        print()
        p_coun = int(input('Enter player count (> 1 and < 12): '))
        if p_coun < 2 or p_coun > 11:
            raise ValueError
        else:
            return p_coun
    except ValueError:
        print('Enter Only > 1 and < 12 Integer Value')
        return p_c()
def p_n(i):
    print()
    p1 = input('Enter player '+str(i)+' name: ')
    if p1 == '':
        print('Input cannot be empty')
        return p_n(i)
    elif len(p1) > 10:
        print('write with in 10 chars')
        return p_n(i)
    else:
        return p1
def get(s,l):
    try:
        print()
        c = int(input('Enter ' + s))
        if c not in l:
            raise ValueError
        else:
            return c
    except ValueError:
        print('Enter only given value')
        return get(s, l)
def get_in(st,players,a,lis):
    try:
        print()
        g = int(input(players[a] + st))
        if g not in lis:
            raise ValueError
        else:
            return g
    except ValueError:
        print('Enter Correct Value')
        return get_in(st, players, a, lis)
def play():
    import random
    import math
    print()
    q = int(input('Want to play as Indian Team? (1 - yes/ 0 - no) : '))
    if q == 1:
        players = ['Rohit','Gill','Kohli','Shreyas','KL Rahul','Hardik','Jadeja','Ashwin','Shami','Bumrah','Siraj']
        p_count = 11
    elif q == 0:
        players = []
        p_count = p_c()
        print('\n')
        for i in range(1,p_count + 1):
            p = p_n(i)
            players.append(p)
    else:
        raise ValueError
    overs = ov()
    o_runs = 0
    p_out = [0] * p_count
    p_runs = [0] * p_count
    p_balls = [0] * p_count
    p_lo = [0] * p_count
    p_overs = [0] * p_count
    p_rpo =[0] * p_count
    p_wickets = [0] * p_count
    Inns = toss()
    total1 = 0
    total2 = 0
    wickets1 = 0
    wickets2 = 0
    a = 0
    b = 0
    over1 = 0.0
    over2 = 0.0
    runs = [0,1,2,3,4,5,6]
    l = []
    
    
    if Inns == 'BAT':
        
        print()
        for index, value in enumerate(players):
            if p_out[index] == 0:
                l.append(index)
                print('Enter',index, "for", value)
        a = get('stricker -', l)
        l.clear()
        p_out[a] = 1
        print()
        for index, value in enumerate(players):
            if p_out[index] == 0:
                l.append(index)
                print('Enter',index, "for", value)
        b = get('Non-stricker -', l)
        l.clear()
        p_out[b] = 1
        for i in range(1,(overs * 6) + 1):
            print()
            print('SCORE -',total1,'/',wickets1,'OVERS -', round(over1,1))
            print(players[a],'Score -',p_runs[a])
            run1 = get_in(' Hit a run(0,1,2,3,4,5,6): ', players, a, runs)
            out1 = random.choices(runs, weights= [1,2,3,6,10,20,16])
            out = out1[0]
            print('PC Bowl -',out)
            
            if run1 != out:
                over1 += 0.1
                p_balls[a] += 1 
                total1 += run1
                p_runs[a] += run1
                if run1 == 1 or run1 == 3:
                    a,b = b,a
                o = over1 - math.trunc(over1)
                if round(o,1) == 0.6:
                    over1 = over1 + 1.0
                    over1 = over1 - 0.6
                    a,b = b,a
                if i == overs * 6:
                    print('\n')
                    print('Innings Break')
                    bat_card(players,p_runs,p_out, p_balls)
                    print('YOUR SCORE -',total1,'/',wickets1,'OVERS -', round(over1,1))
                    print('PC TARGET -', total1 + 1)
            else:
                wickets1 += 1
                over1 += 0.1
                p_balls[a] += 1
                p_out[a] = 2
                print(players[a],'Out!!!')
                print(players[a],'Score -',p_runs[a])
                if i != overs * 6 and p_count - 1 != wickets1:
                    print('\n')
                    print('SCORE -',total1,'/',wickets1,'OVERS -', round(over1,1))
                    for index, value in enumerate(players):
                        if p_out[index] == 0:
                            l.append(index)
                            print('Enter',index, "for", value)
                    a = get('batsman -', l)
                    l.clear()
                    p_out[a] = 1
                o = over1 - math.trunc(over1)
                if round(o,1) == 0.6:
                    over1 = over1 + 1.0
                    over1 = over1 - 0.6
                    a,b = b,a
                if p_count - 1 == wickets1:
                    print('\n')
                    print('---ALL OUT---')
                    print('Innings Break')
                    bat_card(players,p_runs,p_out,p_balls)
                    print('YOUR SCORE -',total1,'/',wickets1,'OVERS -', round(over1,1))
                    print('PC TARGET -', total1 + 1)
                    break
                if i == overs * 6:
                    print('\n')
                    print('Innings Break')
                    bat_card(players,p_runs,p_out,p_balls)
                    print('YOUR SCORE -',total1,'/',wickets1,'OVERS -', round(over1,1))
                    print('PC TARGET -', total1 + 1)
        
        print('\n')
        for index, value in enumerate(players):
            l.append(index)
            print('Enter',index, "for", value)
        a = get('bowler - ', l)
        l.clear()
        p_lo[a] = 1
        
        for i in range(1,(overs * 6) + 1):
            print()
            print('PC need',total1 + 1 - total2,'Runs in',overs * 6 - (i-1),'Balls')
            print('SCORE -',total2,'/',wickets2,'OVERS -', round(over2,1))
            bowl = get_in(' Bowl a ball(0,1,2,3,4,5,6): ', players, a, runs)
            run2 = random.choice(runs)
            print('PC Hits',run2)
            if run2 != bowl:
                over2 += 0.1
                p_overs[a] += 0.1
                total2 += run2
                p_rpo[a] += run2
                o_runs += run2
                o = over2 - math.trunc(over2) 
                if round(o,1) == 0.6:
                    over2 = over2 + 1.0
                    over2 = over2 - 0.6
                    p_overs[a] -= 0.6
                    p_overs[a] += 1
                    if i != overs * 6 and total2 < total1:
                        print()
                        print('This over',o_runs,'Runs' )
                        o_runs = 0
                        print()
                        print('SCORE -',total2,'/',wickets2,'OVERS -', round(over2,1))
                        for index, value in enumerate(players):
                            if p_lo[index] == 0:
                                l.append(index)
                                print('Enter',index, "for", value)
                        p_lo[a] = 0
                        a = get('bowler - ', l)
                        p_lo[a] = 1
                        l.clear()
                if total2 > total1:
                    print('\n')
                    print('***YOU LOSS***')
                    bat_card(players,p_runs,p_out,p_balls)
                    bowl_card(players,p_wickets,p_overs,p_rpo)
                    print('YOUR SCORE -',total1,'/',wickets1,'OVERS -', round(over1,1))
                    print('PC SCORE -',total2,'/',wickets2,'OVERS -', round(over2,1))
                    print('PC WON BY', (p_count - 1) - wickets2,'wickets')
                    break
                
                if i == overs * 6:
                    if total2 == total1:
                        print('\n')
                        print('***MATCH TIE***')
                        bat_card(players,p_runs,p_out,p_balls)
                        bowl_card(players,p_wickets,p_overs,p_rpo)
                        print('YOUR SCORE -',total1,'/',wickets1,'OVERS -', round(over1,1))
                        print('PC SCORE -',total2,'/',wickets2,'OVERS -', round(over2,1))
                        print('You Won by', total1-total2,'Runs')
                        break
                    else:
                        print('\n')
                        print('***YOU WON***')
                        bat_card(players,p_runs,p_out,p_balls)
                        bowl_card(players,p_wickets,p_overs,p_rpo)
                        print('YOUR SCORE -',total1,'/',wickets1,'OVERS -', round(over1,1))
                        print('PC SCORE -',total2,'/',wickets2,'OVERS -', round(over2,1))
                        print('You Won by', total1-total2,'Runs')
            else:
                wickets2 += 1
                p_wickets[a] = p_wickets[a] + 1
                over2 += 0.1
                p_overs[a] += 0.1
                print('Out!!!')
                o = over2 - math.trunc(over2)
                if round(o,1) == 0.6:
                    over2 = over2 + 1.0
                    over2 = over2 - 0.6
                    p_overs[a] -= 0.6
                    p_overs[a] += 1
                    if i != overs * 6 and p_count -1 != wickets2:
                        print()
                        print('This over',o_runs,'Runs' )
                        o_runs = 0
                        print()
                        print('SCORE -',total2,'/',wickets2,'OVERS -', round(over2,1))
                        for index, value in enumerate(players):
                            if p_lo[index] == 0:
                                l.append(index)
                                print('Enter',index, "for", value)
                        p_lo[a] = 0
                        a = get('bowler', l)
                        p_lo[a] = 1
                        l.clear()
                if p_count - 1 == wickets2:
                    print('\n')
                    print('---ALL OUT---')
                    print('***YOU WON***')
                    print('PC SCORE -',total2,'/',wickets2,'OVERS -', round(over2,1))
                    bat_card(players,p_runs,p_out,p_balls)
                    bowl_card(players,p_wickets,p_overs,p_rpo)
                    print('YOUR SCORE -',total1,'/',wickets1,'OVERS -', round(over1,1))
                    print('You Won by', total1-total2,'Runs')
                    break
                if i == overs * 6:
                    if total2 == total1:
                        print('\n')
                        print('***MATCH TIE***')
                        bat_card(players,p_runs,p_out,p_balls)
                        bowl_card(players,p_wickets,p_overs,p_rpo)
                        print('YOUR SCORE -',total1,'/',wickets1,'OVERS -', round(over1,1))
                        print('PC SCORE -',total2,'/',wickets2,'OVERS -', round(over2,1))
                        print('You Won by', total1-total2,'Runs')
                        break
                    else:
                        print('\n')
                        print('***YOU WON***')
                        bat_card(players,p_runs,p_out,p_balls)
                        bowl_card(players,p_wickets,p_overs,p_rpo)
                        print('YOUR SCORE -',total1,'/',wickets1,'OVERS -', round(over1,1))
                        print('PC SCORE -',total2,'/',wickets2,'OVERS -', round(over2,1))
                        print('You Won by', total1-total2,'Runs')
        
        
    else:
        
        print('\n')
        for index, value in enumerate(players):
            l.append(index)
            print('Enter',index, "for", value)
        a = get('bowler - ', l)
        l.clear()
        p_lo[a] = 1
        for i in range(1,(overs * 6) + 1):
            print()
            print('SCORE -',total1,'/',wickets1,'OVERS -', round(over1,1))
            bowl = get_in(' Bowl a ball(0,1,2,3,4,5,6): ', players, a, runs)
            run1 = random.choice(runs)
            print('PC Hits',run1)
            if run1 != bowl:
                over1 += 0.1
                p_overs[a] += 0.1
                total1 += run1
                p_rpo[a] += run1
                o_runs += run1
                o = over1 - math.trunc(over1) 
                if round(o,1) == 0.6:
                    over1 = over1 + 1.0
                    over1 = over1 - 0.6
                    p_overs[a] -= 0.6
                    p_overs[a] += 1
                    if i != overs * 6:
                        print()
                        print('This over',o_runs,'Runs' )
                        o_runs = 0
                        print()
                        print('SCORE -',total1,'/',wickets1,'OVERS -', round(over1,1))
                        for index, value in enumerate(players):
                            if p_lo[index] == 0:
                                l.append(index)
                                print('Enter',index, "for", value)
                        p_lo[a] = 0
                        a = get('bowler - ', l)
                        p_lo[a] = 1
                        l.clear()
                if i == overs * 6:
                    print('\n')
                    print('Innings Break')
                    print('PC SCORE -',total1,'/',wickets1,'OVERS -', round(over1,1))
                    bowl_card(players,p_wickets,p_overs,p_rpo)
                    print('YOUR TARGET -',total1 + 1)
                    print('\n')
                    break
                       
            else:
                wickets1 += 1
                over1 += 0.1
                p_overs[a] += 0.1
                p_wickets[a] = p_wickets[a] + 1
                print('Out!!!')
                o = over1 - math.trunc(over1)
                if round(o,1) == 0.6:
                    over1 = over1 + 1.0
                    over1 = over1 - 0.6
                    p_overs[a] -= 0.6
                    p_overs[a] += 1
                    if i != overs * 6 and p_count - 1 != wickets1:
                        print()
                        print('This over',o_runs,'Runs' )
                        o_runs = 0
                        print()
                        print('SCORE -',total1,'/',wickets1,'OVERS -', round(over1,1))
                        for index, value in enumerate(players):
                            if p_lo[index] == 0:
                                l.append(index)
                                print('Enter',index, "for", value)
                        p_lo[a] = 0
                        a = get('bowler', l)
                        p_lo[a] = 1
                        l.clear()
                if p_count - 1 == wickets1:
                    print('\n')
                    print('---ALL OUT---')
                    print('Innings Break')
                    print('PC SCORE -',total1,'/',wickets1,'OVERS -', round(over1,1))
                    bowl_card(players,p_wickets,p_overs,p_rpo)
                    print('YOUR TARGET -',total1 + 1)

                    break
                if i == overs * 6:
                    print('\n')
                    print('Innings Break')
                    print('PC SCORE -',total1,'/',wickets1,'OVERS -', round(over1,1))
                    bowl_card(players,p_wickets,p_overs,p_rpo)
                    print('YOUR TARGET -',total1 + 1)
                    
        print('\n')
        for index, value in enumerate(players):
            if p_out[index] == 0:
                l.append(index)
                print('Enter',index, "for", value)
        a = get('stricker -', l)
        l.clear()
        print()
        p_out[a] = 1
        for index, value in enumerate(players):
            if p_out[index] == 0:
                l.append(index)
                print('Enter',index, "for", value)
        b = get('Non-stricker -', l)
        l.clear()
        p_out[b] = 1
        for i in range(1,(overs * 6) + 1):
            print()
            print('YOUR TARGET -',total1 + 1)
            print('YOU need',total1 + 1 - total2,'Runs in',overs * 6 - (i-1),'Balls')
            print('SCORE -',total2,'/',wickets2,'OVERS -', round(over2,1))
            print(players[a],'Score -',p_runs[a])
            run2 = get_in(' Hit a run(0,1,2,3,4,5,6): ', players, a, runs)
            out1 = random.choices(runs, weights= [1,2,3,6,10,20,16])
            out = out1[0]
            print('PC Bowl -',out)
            
            if run2 != out:
                over2 += 0.1
                p_balls[a] += 1
                total2 += run2
                p_runs[a] += run2
                if run2 == 1 or run2 == 3:
                    a,b = b,a
                o = over2 - math.trunc(over2) 
                if round(o,1) == 0.6:
                    over2 = over2 + 1.0
                    over2 = over2 - 0.6
                    a,b = b,a
                if total2 > total1:
                    print('\n')
                    print('***YOU WON***')
                    print('YOUR SCORE -',total2,'/',wickets2,'OVERS -', round(over2,1))
                    print('PC SCORE -',total1,'/',wickets1,'OVERS -', round(over1,1))
                    bat_card(players,p_runs,p_out,p_balls)
                    bowl_card(players,p_wickets,p_overs,p_rpo)
                    print('YOU WON BY', (p_count - 1) - wickets2,'wickets')
                    break
                if i == overs * 6:
                    if total2 == total1:
                        print('\n')
                        print('***MATCH TIE***')
                        bat_card(players,p_runs,p_out,p_balls)
                        bowl_card(players,p_wickets,p_overs,p_rpo)
                        print('YOUR SCORE -',total2,'/',wickets2,'OVERS -', round(over2,1))
                        print('PC SCORE -',total1,'/',wickets1,'OVERS -', round(over1,1))
                        print('PC Won by', total1-total2,'Runs')
                        break
                    else:
                        print('\n')
                        print('***YOU LOSS***')
                        print('PC SCORE -',total1,'/',wickets1,'OVERS -', round(over1,1))
                        print('YOUR TARGET -', total1 + 1)
                        bat_card(players,p_runs,p_out,p_balls)
                        bowl_card(players,p_wickets,p_overs,p_rpo)
                        print('YOUR SCORE -',total2,'/',wickets2,'OVERS -', round(over2,1))
                        print('PC Won by', total1-total2,'Runs')
            
            else:
                
                
                wickets2 += 1
                over2 += 0.1
                p_balls[a] += 1
                p_out[a] = 2
                print(players[a],'Out!!!')
                print(players[a],'Score -',p_runs[a])
                if i != overs * 6 and p_count - 1 != wickets2:
                    print()
                    print('SCORE -',total2,'/',wickets2,'OVERS -', round(over2,1))
                    for index, value in enumerate(players):
                        if p_out[index] == 0:
                            l.append(index)
                            print('Enter',index, "for", value)
                    a = get('batsman -', l)
                    l.clear()
                    p_out[a] = 1
                o = over2 - math.trunc(over2)
                if round(o,1) == 0.6:
                    over2 = over2 + 1.0
                    over2 = over2 - 0.6
                    a,b = b,a
                if p_count - 1 == wickets2:
                    print('\n')
                    print('---ALL OUT---')
                    print('***YOU LOSS***')
                    print('PC SCORE -',total1,'/',wickets1,'OVERS -', round(over1,1))
                    print('YOUR TARGET -', total1 + 1)
                    bat_card(players,p_runs,p_out,p_balls)
                    bowl_card(players,p_wickets,p_overs,p_rpo)
                    print('YOUR SCORE -',total2,'/',wickets2,'OVERS -', round(over2,1))
                    print('PC Won by', total1-total2,'Runs')
                    break
                if i == overs * 6:
                    if total2 == total1:
                        print('\n')
                        print('***MATCH TIE***')
                        bat_card(players,p_runs,p_out,p_balls)
                        bowl_card(players,p_wickets,p_overs,p_rpo)
                        print('YOUR SCORE -',total2,'/',wickets2,'OVERS -', round(over2,1))
                        print('PC SCORE -',total1,'/',wickets1,'OVERS -', round(over1,1))
                        print('PC Won by', total1-total2,'Runs')
                        break
                    else:
                        print('\n')
                        print('***YOU LOSS***')
                        print('PC SCORE -',total1,'/',wickets1,'OVERS -', round(over1,1))
                        print('YOUR TARGET -', total1 + 1)
                        bat_card(players,p_runs,p_out,p_balls)
                        bowl_card(players,p_wickets,p_overs,p_rpo)
                        print('YOUR SCORE -',total2,'/',wickets2,'OVERS -', round(over2,1))
                        print('PC Won by', total1-total2,'Runs')
def con():
    try:
        w = input("Want to play Next Match (yes/no): ")
        if w.lower() == 'yes' or w.lower() == 'y':
            cric()
        elif w.lower() == 'no'or w.lower() == 'n':
            print('Thank you for Playing....')
        else:
            raise ValueError
    except ValueError:
        print('Enter Correct Value')
        return cric()
def cric():
    try:
        play()
        con()
    except ValueError:
        print('Enter Correct Value')
        return cric()
cric()

