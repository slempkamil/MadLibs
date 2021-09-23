from tkinter import *

root = Tk()
root.geometry('400x300')
root.title('MadLibs Generator')
Label(root, text='MadLibs Generator', font='arial 20 bold').pack()
Label(root, text='Choose one:', font='arial 15 bold').place(x=40, y=80)


def madlib1():
    noun1 = input('enter a noun(plural) : ')
    place = input('enter a place : ')
    noun2 = input('enter a noun : ')
    noun3 = input('enter a noun(plural) : ')
    noun4 = input('enter a noun : ')
    adjective1 = input('enter an adjective : ')
    verb1 = input('enter a verb : ')
    number = input('enter a number : ')
    adjective2 = input('enter an adjective : ')
    body_part = input('enter a body part : ')
    verb2 = input('enter a verb : ')

    print('Two ' + noun1 + ', both alike in dignity,\n' +
          'In fair ' + place + ', where we lay our scene,\n' +
          'From ancient ' + noun2 + ' break to new mutiny,\n' +
          'Where civil blood makes civil hands unclean.\n' +
          'From forth the fatal loins of these two foes\n' +
          'A pair of star-cross`d ' + noun3 + ' take their life;\n' +
          'Whole misadventured piteous overthrows\n' +
          'Do with their ' + noun4 + ' bury their parents` strife.\n' +
          'The fearful passage of their ' + adjective1 + ' love\n' +
          'And the continuance of their parents` rage,\n' +
          'Which, but their children`s end, nought could ' + verb1 + ',\n' +
          'Is now the ' + number + ' hours` traffic of our stage;' +
          'The which if you with ' + adjective2 + ' ' + body_part + 'attend,\n' +
          'What here shall ' + verb2 + ', our toil shall strive to mend.'
          )


def madlib2():
    adjective = input('enter an adjective : ')
    noun = input('enter a noun : ')
    animal = input('enter an animal : ')
    noise = input('enter a noise : ')

    print(adjective + ' Macdonald had a ' + noun + ', E-I-E-I-O\n' +
          'and on that ' + noun + ' he had an ' + animal + ', E-I-E-I-O\n' +
          'with a ' + noise + ' ' + noise + ' here\n' +
          'and a ' + noise + ' ' + noise + ' there,\n' +
          'here a ' + noise + ', there a ' + noise + ',\n' +
          'everywhere a ' + noise + ' ' + noise + ',\n' +
          adjective + ' Macdonald had a ' + noun + ', E-I-E-I-O.'

          )


Button(root, text="Romeo and Juliet:Prologue", font='arial 15', command=madlib1, bg='ghost white').place(x=60, y=120)
Button(root, text="Old Macdonald", font='arial 15', command=madlib2, bg='ghost white').place(x=60, y=165)

root.mainloop()
