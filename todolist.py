import flet as ft

def main(page: ft.Page):
    # Configure page settings
    page.title = "My To-Do App"
    page.bgcolor = "#f0f8ff"  # AliceBlue background
    page.padding = 20
    page.horizontal_alignment = "center"
    page.vertical_alignment = "spaceBetween"  # This helps with footer placement

    def add_clicked(e):
        if new_task.value:
            page.add(
                ft.Container(
                    ft.Checkbox(
                        label=new_task.value,
                        fill_color="#EE82EE", # Box color purple
                        check_color="#ffffff",
                    ),
                    bgcolor="#ffe66d",
                    padding=10,
                    border_radius=10,
                    margin=5,
                    animate=ft.animation.Animation(300, "easeInOut"),
                )
            )
            new_task.value = ""
            page.update()

    # Create footer
    footer = ft.Container(
        ft.Text(
            "Crafted by Muhammad Tariq Mahboob",
            size=25,
            color="#006400",
            italic=True,
        ),
        padding=10,
        alignment=ft.alignment.center,
    )

    new_task = ft.TextField(
        hint_text="What needs to be done?",
        width=300,
        bgcolor="#ffffff",
        color="#333333",
        border_color="#4ecdc4",
        focused_border_color="#ff6b6b",
        border_radius=10,
        cursor_color="#ff6b6b",
    )

    add_button = ft.FloatingActionButton(
        icon=ft.icons.ADD,
        on_click=add_clicked,
        bgcolor="#4ecdc4",
        tooltip="Add task",
        shape=ft.CircleBorder(),
        width=60,
        height=60,
    )

    header = ft.Text(
        "My Colorful To-Do List",
        size=24,
        weight="bold",
        color="#ff6b6b",
        text_align="center",
    )

    # Main content column
    main_content = ft.Column(
        [
            header,
            ft.Row(
                [new_task, add_button],
                alignment="center",
                spacing=10,
            ),
        ],
        spacing=20,
    )

    # Create a column that holds main content and pushes footer to bottom
    page.add(
        ft.Column(
            [
                main_content,
                ft.Container(expand=True),  # This pushes the footer down
                footer
            ],
            expand=True,
        )
    )

ft.app(main)