from App import App


def main() -> None:
    app = App()
    app.unpack()
    app.root.mainloop()
    #game1 = Game(105)
    #test1 = Test(game1, 10)
    #test1.check_rules(game1)

    #test1.hawk_vs_dove()
    #test1.hawk_vs_hawk()
    #test1.dove_vs_dove()
    #test1.dove_vs_no_one()
    #test1.hawk_vs_no_one()
    #test1.no_one_vs_no_one()
    #habitat1 = Habitat(2, 2, game1)
    #habitat1.simulate(120)
    #habitat1.make_encounters()

if __name__ == "__main__":
    main()
