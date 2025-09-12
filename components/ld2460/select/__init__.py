import esphome.codegen as cg
from esphome.components import select
import esphome.config_validation as cv
from esphome.const import CONF_BAUD_RATE, ENTITY_CATEGORY_CONFIG, ICON_THERMOMETER, CONF_MODE, CONF_SENSITIVITY

from .. import CONF_LD2460_ID, LD2460Component, ld2460_ns

DEPENDENCIES = ["ld2460"]

ModeSelect = ld2460_ns.class_("ModeSelect", select.Select)
BaudRateSelect = ld2460_ns.class_("BaudRateSelect", select.Select)
SensitivitySelect = ld2460_ns.class_("SensitivitySelect", select.Select)

CONFIG_SCHEMA = {
    cv.GenerateID(CONF_LD2460_ID): cv.use_id(LD2460Component),
    cv.Optional(CONF_MODE): select.select_schema(
        ModeSelect,
        entity_category=ENTITY_CATEGORY_CONFIG,
        icon=ICON_THERMOMETER, #fixme
    ),
    cv.Optional(CONF_BAUD_RATE): select.select_schema(
        BaudRateSelect,
        entity_category=ENTITY_CATEGORY_CONFIG,
        icon=ICON_THERMOMETER,
    ),
    cv.Optional(CONF_SENSITIVITY): select.select_schema(
        SensitivitySelect,
        entity_category=ENTITY_CATEGORY_CONFIG,
        icon=ICON_THERMOMETER,
    ),
}


async def to_code(config):
    ld2460_component = await cg.get_variable(config[CONF_LD2460_ID])

    if mode_config := config.get(CONF_MODE):
        s = await select.new_select(
            mode_config,
            options=[
                "Side",
                "Top",
            ],
        )
        await cg.register_parented(s, config[CONF_LD2460_ID])
        cg.add(ld2460_component.set_mode_select(s))
    if baud_rate_config := config.get(CONF_BAUD_RATE):
        s = await select.new_select(
            baud_rate_config,
            options=[
                "9600",
                "19200",
                "38400",
                "57600",
                "115200",
                "230400",
                "256000",
                "460800",
            ],
        )
        await cg.register_parented(s, config[CONF_LD2460_ID])
        cg.add(ld2460_component.set_baud_rate_select(s))
    if sensitivity_config := config.get(CONF_SENSITIVITY):
        s = await select.new_select(
            sensitivity_config,
            options=[
                "Low",
                "Medium",
                "High",
            ],
        )
        await cg.register_parented(s, config[CONF_LD2460_ID])
        cg.add(ld2460_component.set_sensitivity_select(s))