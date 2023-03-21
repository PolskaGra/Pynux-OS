def Dir_Check(Command):
    global first
    if Command.startswith("C:\\", 0, 3):
        first = True
    elif Command.startswith("c:\\", 0, 3):
        first = True
    elif Command.startswith("B:\\", 0, 3):
        first = True
    elif Command.startswith("b:\\", 0, 3):
        first = True
    elif Command.startswith("D:\\", 0, 3):
        first = True
    elif Command.startswith("d:\\", 0, 3):
        first = True
    elif Command.startswith("E:\\", 0, 3):
        first = True
    elif Command.startswith("e:\\", 0, 3):
        first = True
    elif Command.startswith("F:\\", 0, 3):
        first = True
    elif Command.startswith("f:\\", 0, 3):
        first = True
    elif Command.startswith("G:\\", 0, 3):
        first = True
    elif Command.startswith("g:\\", 0, 3):
        first = True
    elif Command.startswith("H:\\", 0, 3):
        first = True
    elif Command.startswith("h:\\", 0, 3):
        first = True
    elif Command.startswith("I:\\", 0, 3):
        first = True
    elif Command.startswith("i:\\", 0, 3):
        first = True
    elif Command.startswith("J:\\", 0, 3):
        first = True
    elif Command.startswith("j:\\", 0, 3):
        first = True
    elif Command.startswith("K:\\", 0, 3):
        first = True
    elif Command.startswith("k:\\", 0, 3):
        first = True
    elif Command.startswith("L:\\", 0, 3):
        first = True
    elif Command.startswith("l:\\", 0, 3):
        first = True
    elif Command.startswith("M:\\", 0, 3):
        first = True
    elif Command.startswith("m:\\", 0, 3):
        first = True
    elif Command.startswith("N:\\", 0, 3):
        first = True
    elif Command.startswith("n:\\", 0, 3):
        first = True
    elif Command.startswith("O:\\", 0, 3):
        first = True
    elif Command.startswith("o:\\", 0, 3):
        first = True
    elif Command.startswith("P:\\", 0, 3):
        first = True
    elif Command.startswith("p:\\", 0, 3):
        first = True
    elif Command.startswith("Q:\\", 0, 3):
        first = True
    elif Command.startswith("q:\\", 0, 3):
        first = True
    elif Command.startswith("R:\\", 0, 3):
        first = True
    elif Command.startswith("r:\\", 0, 3):
        first = True
    elif Command.startswith("S:\\", 0, 3):
        first = True
    elif Command.startswith("s:\\", 0, 3):
        first = True
    elif Command.startswith("T:\\", 0, 3):
        first = True
    elif Command.startswith("t:\\", 0, 3):
        first = True
    elif Command.startswith("U:\\", 0, 3):
        first = True
    elif Command.startswith("u:\\", 0, 3):
        first = True
    elif Command.startswith("V:\\", 0, 3):
        first = True
    elif Command.startswith("v:\\", 0, 3):
        first = True
    elif Command.startswith("W:\\", 0, 3):
        first = True
    elif Command.startswith("w:\\", 0, 3):
        first = True
    elif Command.startswith("X:\\", 0, 3):
        first = True
    elif Command.startswith("x:\\", 0, 3):
        first = True
    elif Command.startswith("Y:\\", 0, 3):
        first = True
    elif Command.startswith("y:\\", 0, 3):
        first = True
    elif Command.startswith("Z:\\", 0, 3):
        first = True
    elif Command.startswith("z:\\", 0, 3):
        first = True
    else:
        first = False
