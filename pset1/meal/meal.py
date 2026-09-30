def main():
    user_time = convert(input("What time is it? ").strip())
    
    if user_time >= 7 and user_time <= 8:
        print("breakfast time ")
    elif user_time >= 12 and user_time <= 13:
        print("lunch time")
    elif user_time >= 18 and user_time <= 19:
        print("dinner time")
    else:
        pass




def convert(time):
   hours, minutes = time.split(":")
   hours = float(hours)
   minutes = float(minutes)
   minutes_in_hours = minutes / 60
   total = minutes_in_hours + hours
   return total
        
    


if __name__ == "__main__":
    main()