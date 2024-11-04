from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='listener',
            namespace='client_node_reset',
            executable='client',
            name='Reset'
        ),
        Node(
            package='listener',
            namespace='listener_node',
            executable='listener',
            name='Listener'
        ),
        Node(
            package='listener',
            namespace='client_clear_node',
            executable='clientClear',
            name='Clear'
        ),
        Node(
            package='listener',
            namespace='client_draw_node',
            executable='clientDraw',
            name='DrawUndraw'
        )
    ])
