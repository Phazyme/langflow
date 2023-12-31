from typing import Optional

from langflow.template.field.base import TemplateField
from langflow.template.frontend_node.base import FrontendNode


class MemoryFrontendNode(FrontendNode):
    #! Needs testing
    def add_extra_fields(self) -> None:
        # add return_messages field
        self.template.add_field(
            TemplateField(
                field_type="bool",
                required=False,
                show=True,
                name="return_messages",
                advanced=False,
                value=False,
            )
        )

    @staticmethod
    def format_field(field: TemplateField, name: Optional[str] = None) -> None:
        FrontendNode.format_field(field, name)

        if not isinstance(field.value, str):
            field.value = None
        if field.name == "k":
            field.required = True
            field.show = True
            field.field_type = "int"
            field.value = 10
            field.display_name = "Memory Size"
        field.password = False
        if field.name == "return_messages":
            field.required = False
            field.show = True
            field.advanced = False
