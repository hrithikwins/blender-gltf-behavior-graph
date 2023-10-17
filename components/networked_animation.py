from io_hubs_addon.components.hubs_component import HubsComponent
from io_hubs_addon.components.types import Category, NodeType, PanelType
from ..utils import do_register, do_unregister


class NetworkedAnimation(HubsComponent):
    _definition = {
        'name': 'networked-animation',
        'display_name': 'BG Networked Animation',
        'category': Category.OBJECT,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'RENDER_ANIMATION',
        'version': (1, 0, 0),
        'deps': ['networked']
    }

    def draw(self, context, layout, panel):
        row = layout.row()
        row.label(text="Network animation updates on this object.")


def register():
    do_register(NetworkedAnimation)


def unregister():
    do_unregister(NetworkedAnimation)
