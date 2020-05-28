label start:
    python:
        player= "MC"
        s_name = "Sayori"
        m_name = "Monika"
        n_name = "Natsuki"
        y_name = "Yuri"
        # Controls whether we have a Menu in the Textbox
        quick_menu = True
        # Controls whether we want normal or glitched dialogue
        style.say_dialogue = style.normal
        # Controls whether Sayori is Dead. Leave this alone
        in_sayori_kill = None
        # Controls whether we allow skipping.
        allow_skipping = True
        config.allow_skipping = True
    call test_menu from _call_test_menu
    
    
label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
