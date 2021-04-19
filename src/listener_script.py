import time
from rlbot.agents.base_script import BaseScript
from rlbot.utils.game_state_util import GameState


# Extending the BaseScript class is purely optional. It's just convenient / abstracts you away from
# some strange classes like GameInterface

class ListenerScript(BaseScript):
    def __init__(self):
        super().__init__("ListenerBot")

    def run(self):
        # state setting
        self.set_game_state(GameState(console_commands=["Stat FPS"]))

        while True:
            time.sleep(0.5)

            # updating packet
            packet = self.get_game_tick_packet()

            # rendering
            color = self.renderer.white()
            text = f"seconds_elapsed : {packet.game_info.seconds_elapsed}"
            self.game_interface.renderer.begin_rendering()
            self.game_interface.renderer.draw_string_2d(20, 200, 2, 2, text, color)
            self.game_interface.renderer.end_rendering()


    # You can use this __name__ == '__main__' thing to ensure that the script doesn't start accidentally if you
    # merely reference its module from somewhere
if __name__ == "__main__":
    script = ListenerScript()
    script.run()