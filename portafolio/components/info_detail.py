import reflex as rx
from portafolio.components.icon_badge import icon_badge
from portafolio.components.icon_button import icon_button
from portafolio.data import Info
from portafolio.styles.styles import IMAGE_HEIGHT, EmSize, Size


def info_detail(info: Info) -> rx.Component:
    # Build optional components using Python conditionals (static data, not reactive State)
    tech_badges = []
    if info.technologies:
        tech_badges = [
            rx.flex(
                *[
                    rx.badge(
                        rx.box(class_name=technology.icon),
                        technology.name,
                        color_scheme="gray"
                    )
                    for technology in info.technologies
                ],
                wrap="wrap",
                spacing=Size.SMALL.value
            )
        ]

    link_buttons = []
    if info.url:
        link_buttons.append(icon_button("link", info.url))
    if info.github:
        link_buttons.append(icon_button("github", info.github))

    image_components = []
    if info.image:
        image_components.append(
            rx.image(
                src=info.image,
                height=IMAGE_HEIGHT,
                width="auto",
                border_radius=EmSize.DEFAULT.value,
                object_fit="cover"
            )
        )

    side_components = []
    if info.date:
        side_components.append(rx.badge(info.date))
    if info.certificate:
        side_components.append(
            icon_button(
                "shield-check",
                info.certificate,
                solid=True
            )
        )

    return rx.flex(
        rx.hstack(
            icon_badge(info.icon),
            rx.vstack(
                rx.text.strong(info.title),
                rx.text(info.subtitle),
                rx.text(
                    info.description,
                    size=Size.SMALL.value,
                    color_scheme="gray"
                ),
                *tech_badges,
                rx.hstack(*link_buttons),
                spacing=Size.SMALL.value,
                width="100%"
            ),
            spacing=Size.DEFAULT.value,
            width="100%"
        ),
        *image_components,
        rx.vstack(
            *side_components,
            spacing=Size.SMALL.value,
            align="end"
        ),
        flex_direction=["column-reverse", "row"],
        spacing=Size.DEFAULT.value,
        width="100%"
    )
