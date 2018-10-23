#!/usr/bin/env python

values = [6.3, 4.1, 9.7, 0, 8.2, 'abc', 7.7]

for v in values:
    try:
        result = 23.45 / v
    except ZeroDivisionError as err:
        print("UH-OH", err)
        exit()
    except (TypeError, ValueError) as err:
        print(err)
    except Exception as err:
        print("Huh!", err)
    else:
        print(result)
    finally:
        print("processed", v)
