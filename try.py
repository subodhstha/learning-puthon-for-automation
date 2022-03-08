def main():
    marksmath = int(input("Enter marks in maths:"))
    if marksmath > 100 or marksmath <= 0:
        print("invalide input")
    elif marksmath < 32:
        print("fail")
    elif marksmath ==32:
        print ("just pass")
    elif marksmath > 60:
        print("excellent")
    elif marksmath >32:
        print ("passed")
if __name__ == '__main__':
    main()