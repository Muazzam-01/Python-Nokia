main_menu = """
=============== MAIN MENU LIST ====================

        1: Phone book
        2: Message
        3: Chat  
        4: Call register
        5: Tone
        6: Setting 
        7: Call divert
        8: Music
        9: Games
        10:Calculator
        11:Reminders
        12: Clock
        13: Profiles
        14: Services
        15: SIM services

==========
"""

print(main_menu)
main_menu_choice = int(input("ENTER A NUMBER TO CHOOSE: "))

match main_menu_choice:
case 1:
    print("Phone book")
    phone_book = """
  <<<<<<<<<<<<<<  >>>>>>>>>>>>>>>
    1 to Search 
    2 to Service Nos
    3 to Add name
    4 to Erase
    5 to Edit
    6 to Copy
    7 to Assign tone
    8 to Send b'card
    9 to Option 
    10 to Speed dials
    11 to Voice tags
==============
        """

        print(phone_book)
        phone_book_choice = int(input("enter a number to choose"))

        match phone_book_choice:
            case 1:
                print("Search")
            case 2:
                print("Service Nos")
            case 3:
                print("add name")
            case 4:
                print("Erase")
            case 5:
                print("Edit")
            case 6:
                print("Copy")
            case 7:
                print("Assign tone")
            case 8:
                print("Send b'card")
            case 9:
                print("optio
options = """
       press 1 : Memory in use
       press 2 : Type of view
       press 3 : Memmory status
                """

                print(options)
                option = int(input("ENTER A NUMBER CHOOSE "))

                match option_choice:
                    case 1:
                        print("Memory in use")
                    case 2:
                        print("Type of view")
                    case 3:
                        print("Memory status")
                    case _:
                        print("invalid")

            case 10:
                print("Speed dials")
            case 11:
                print("Voice tags")
            case _:
                print("Invalid Entry")

    case 2:
        print("Message")

        message_menu= """
 1 write message
 2 Inbox
 3 Outbox 
 4 Picture message
 5 Template 
 6 Smileys
 7 Message setting
 8 Info service 
 9 Voice mailbox number
 10 Service command editor
        """

        print(message_menu)
        message_ = int(input("message"))

        match message_menu:
            case 1:
                print("Typing message")
            case 2:
                print("Inbox empty")
            case 3:
                print("Outbox empty")
            case 4:
                print("Picture message")
            case 5:
                print("Template empty")
            case 6:
                print("Smileys")
            case 7:
                print("Message setting")

                message_setting = """ 
press 1 : Set
press 2 : Command 
                """

                print(message_setting)
                message_setting_list = int(input("message_setting"))

                match message_setting:
                    case 1:
                        print("Set1")

                        set1 = """
 1 Message centre number
 2 Messages sent as
 3 Message validity
                        """

                        print(set1)
                        message_list = int(input("Set1"))

                        match message_list:
                            case 1:
                                print("Message centre number")
                            case 2:
                                print("Messages sent as")
                            case 3:
                                print("Outbox empty")
                            case _:
                                print("Message validity")

                    case 2:
                        print("Command")

                        common = """
 1 Delivery report
 2 Reply via same centre
 3 Character support
                        """

                        print(common)
                        message_list = int(input("common"))

                        match message_list:
                            case 1:
                                print("Delivery report")
                            case 2:
                                print("Reply via same centre")
                            case 3:
                                print("Outbox empty")
                            case _:
                                print("Character support")

            case 8:
                print("Info service")
            case 9:
                print("Voice mailbox number")
            case 10:
                print("Service command editor")
            case _:
                print("invalid input")

    case 3:
        print("Chat Menu")

    case 4:
        print("call_register")

        call_register = """
press 1 Missed call
press 2 Recieved call
press 3 Dialled number
press 4 Erase recent call lists
press 5 Show call duration
press 6 Show call costs
press 7 Call cost settings
press 8 Prepaid credit
        """

        print(call_register)
        call_register_list = int(input("call register list"))

        match call_register_list:
            case 1:
                print("Missed call")
            case 2:
                print("Recieved call")
            case 3:
                print("Dialled number")
            case 4:
                print("Erase recent call lists")
            case 5:
                print("Show call duration")

                show_call_duration = """
press 1 Last call duration
press 2 All calls' duration
press 3 Received calls
press 4 Dialled calls duration
press 5 Clear times
                """

                print(show_call_duration)
                call_duration_list = int(input("show call duration"))

                match show_call-duration_list:
                    case 1:
                        print("Last call duration")
                    case 2:
                        print("All calls' duration")
                    case 3:
                        print("Received calls")
                    case 4:
                        print("Dialled calls duration")
                    case 5:
                        print("Clear times")
                    case _:
                        print("Invalid")

            case 6:
                print("Show call costs")

                show_call_cost = """
press 1 Last cost 
press 2 All call's cost
press 3 Clear counter
                """

                print(show_call_cost)
                show_call_cost_list = int(input("show call cost"))

                match show_call_cost_list:
                    case 1:
                        print("Last cost")
                    case 2:
                        print("All call's cost")
                    case 3:
                        print("Clear counter")
                    case _:
                        print("Invalid")

            case 7:
                print("Call cost settings")

                call_cost_settings = """
press 1 Call cost limit 
press 2 Show cost in
                """

                print(call_cost_settings)
                call_cost_setting_list = int(input("call cost settings"))

                match call_cost_setting_list:
                    case 1:
                        print("Call cost limit")
                    case 2:
                        print("Show cost in")
                    case _:
                        print("Error")

             case 8:
                print("Prepaid credit")
            case _:
                print("Error")

    case 5:
        print("Tone Menu")

        tone_menu = """
press 1 to Ringing tone 
press 2 to Ringing volume
press 3 to Incoming call alert
press 4 to Message alert tone
press 5 to Keypad tones
press 6 to Warning tone
press 7 to Vibrating alert 
press 8 to Screen Saver 
        """

        print(tone_menu)
        tone_menu_list = int(input("tone menu list"))

        match tone_menu_list:
            case 1:
                print("Ringing tone")
            case 2:
                print("Ringing volume")
            case 3:
                print("Incoming call alert")
            case 4:
                print("Message alert tone")
            case 5:
                print("Keypad tones")
            case 6:
                print("Warning tone")
            case 7:
                print("Vibrating alert")
            case 8:
                print("Screen Saver")
            case _:
                print("error")

    case 6:
        print("Setting Menu")

        setting_menu = """
press 1 to Call setting 
press 2 to Phone setting
press 3 to Security setting
press 4 to Restore factory setting
        """

        print(setting_menu)
        setting_menu_list = int(input("setting menu list"))

        match setting_menu_list:
            case 1:
                print("Call setting")

                call_setting_menu = """
press 1 to Automatic radical
press 2 to Speed dailing
press 3 to Call waiting 
press 4 to Own number sending
press 5 to Phone line in use
press 6 to Automatic answer
                """

                print(call_setting_menu)
                call_setting_menuList = int(input("call setting menu"))

                match call_setting_menu_list:
                    case 1:
                        print("Automatic radical")
                    case 2:
                        print("Speed dailing")
                    case 3:
                        print("Call waiting")
                    case 4:
                        print("Own number sending")
                    case 5:
                        print("Phone line in use")
                    case 6:
                        print("Automatic answer")
                    case _:
                        print("error")

            case 2:
                print("Phone setting")

                phone_setting_menu = """
press 1 to language
press 2 to Call info display
press 3 to Welcome note
press 4 to Network selection
press 5 to Confirms SIM service action
                """

                print(phone_setting_menu)
                phone_setting_menu_list = int(input("phone_setting_menu"))

                match phone_setting_menu_list:
                    case 1:
                        print("language")
                    case 2:
                        print("Call info display")
                    case 3:
                        print("Welcome note")
                    case 4:
                        print("Network selection")
                    case 5:
                        print("Confirms SIM service action")
                    case _:
                        print("error")

            case 3:
                print("Security setting")

                security_setting_menu = """
press 1 to PIN code request
press 2 to Call baring service
press 3 to Fixed dialling
press 4 to Closed user group
press 5 to Security level
press 6 to Change access code
                """

                print(security_setting_menu)
                security_setting_menu_list = int(input("security_setting_menu"))

                match security_setting_menu:
                    case 1:
                        print("PIN code request")
                    case 2:
                        print("Call baring service")
                    case 3:
                        print("Fixed dialling")
                    case 4:
                        print("Closed user group")
                    case 5:
                        print("Security level")
                    case 6:
                        print("Change access code")
                    case _:
                        print("error")

            case 4:
                print("Restore factory setting")
            case _:
                print("error")

    case 7:
        print("Call divert Menu")

    case 8:
        print("Music Menu")

        music_menu = """
press 1 to Music player 
press 2 to Radio
press 3 to Recorder
press 4 to Track list
        """

        print(music_menu)
        music_menu_list = int(input("music_menu"));

        match music_menu_list:
            case 1:
                print("Music player")
            case 2:
                print("Radio")
            case 3:
                print("Recorder")
            case 4:
                print("Track list")
            case _:
                print("error")

    case 9:
        print("Games Menu")

    case 10:
        print("Calculator Menu")

    case 11:
        print("Reminder Menu")

    case 12:
        print("Clock Menu")

        clock_menu = """
press 1 to Alarm clock 
press 2 to Clock setting
press 3 to Date setting
press 4 to Stop watch
press 5 to Countdown timer
press 6 to Auto update of date and time
        """

        print(clock_menu)
        clock_menu_list = int(input("clock_menu"));

        match clock_menu_list:
            case 1:
                print("Alarm clock")
            case 2:
                print("Clock setting")
            case 3:
                print("Date setting")
            case 4:
                print("Stop watch")
            case 5:
                print("Countdown timer")
            case 6:
                print("Auto update of date and time")
            case _:
                print("error")

    case 12:
        print("Profile Menu")

    case 13:
        print("SIM service Menu")

    case _:
        print("Mark")

