from bank import value

def main():
      test_bank()

def test_bank():
        assert value("Hello") == int(0)
        assert value(" Hello ") == int(0)
        assert value("Hello, Newman" ) == int(0)
        assert value("How you doing?") == int(20)
        assert value("What's happening?") == int(100)
        assert value("What's up?") == int(100)

if __name__ == "__main__":
    main()