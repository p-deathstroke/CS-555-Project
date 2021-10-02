#NAME: PREET DABHI#
ged_file = open('project_01.ged','r')
output = open('project_02_output.txt', 'w')
for line in ged_file:
    print (f'--> {line}')
    out = f'--> {line}'
    output.write(out)
    line_words = line.split() 
    if line_words[0] == '0':
        if line_words[1] in ['NOTE','TRLR','HEAD']:
            st =' '.join(line_words[2:])
            print(f'<-- {line_words[0]} | {line_words[1]} | Y | {st} \n') # to print in command line same in below code as well
            out = f'<-- {line_words[0]} | {line_words[1]} | Y | {st} \n'    # to print in output file same in below code as well
            output.write(out)
            continue
        else:
            if(line_words[2] in ['INDI', 'FAM']):
                st1 =' '.join(line_words[3:])
                print(f'<-- {line_words[0]} | {line_words[2]} | Y | {line_words[1]} | {st1} \n')
                out= f'<-- {line_words[0]} | {line_words[2]} | Y | {line_words[1]} | {st1} \n'
                output.write(out)
                continue
            else:
                st =' '.join(line_words[2:])
                print(f'<-- {line_words[0]} | {line_words[1]} | N | {st} \n')
                out = f'<-- {line_words[0]} | {line_words[1]} | N | {st} \n'
                output.write(out)
                continue
    if line_words[0] == '1':
        if line_words[1] in ['FAMC','NAME', 'SEX', 'BIRT', 'CHIL', 'MARR', 'WIFE', 'DEAT', 'DIV', 'FAMS', 'HUSB']:
            st =' '.join(line_words[2:])
            print(f'<-- {line_words[0]} | {line_words[1]} | Y | {st} \n')
            out = f'<-- {line_words[0]} | {line_words[1]} | Y | {st} \n'
            output.write(out)
            continue
        else:
            st =' '.join(line_words[2:])
            print(f'<-- {line_words[0]} | {line_words[1]} | N | {st} \n')
            out = f'<-- {line_words[0]} | {line_words[1]} | N | {st} \n'
            output.write(out)
            continue
    if line_words[0] == '2':
        if line_words[1] in ['DATE']:
            st =' '.join(line_words[2:])
            print(f'<-- {line_words[0]} | {line_words[1]} | Y | {st} \n')
            out = f'<-- {line_words[0]} | {line_words[1]} | Y | {st} \n'
            output.write(out)
            continue
        else:
            st =' '.join(line_words[2:])
            print(f'<-- {line_words[0]} | {line_words[1]} | N | {st} \n')
            out = f'<-- {line_words[0]} | {line_words[1]} | N | {st} \n'
            output.write(out)
            continue