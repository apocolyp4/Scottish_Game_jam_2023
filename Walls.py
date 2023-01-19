import appgamekit as agk

class Walls:
    def __init__(self, vis_editor):
        self.walls = []
        self.vis_editor = vis_editor

    def load(self):
        self.walls = []
        scene_id = self.vis_editor.VisualEditor_scene_id
        for scene_entity in self.vis_editor.scenes[scene_id].entities:
            entity = self.vis_editor.VisualEditor_Entities[scene_entity.index]
            image_name = entity.sImage

            is_wall = agk.find_string_count(image_name.lower(), "wall")
            if is_wall > 1:
                self.walls.append(scene_entity.id)

