import esphome.codegen as cg
from esphome.components import select
import esphome.config_validation as cv
from esphome.const import CONF_DIRECTION, ENTITY_CATEGORY_CONFIG, ICON_THERMOMETER, CONF_BAUD_RATE

from .. import CONF_AS201_ID, AS201Component, as201

DEPENDENCIES = ["as201"]

CONF_UPLOAD_RATE = "upload_rate"

DirectionSelect = as201.class_("DirectionSelect", select.Select)
UploadRateSelect = as201.class_("UploadRateSelect", select.Select)
BaudRateSelect = as201.class_("BaudRateSelect", select.Select)

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_AS201_ID): cv.use_id(AS201Component),
        cv.Optional(CONF_DIRECTION): select.select_schema(
            DirectionSelect,
            entity_category=ENTITY_CATEGORY_CONFIG,
            icon=ICON_THERMOMETER,  # fixme
        ),
        cv.Optional(CONF_UPLOAD_RATE): select.select_schema(
            UploadRateSelect,
            entity_category=ENTITY_CATEGORY_CONFIG,
            icon=ICON_THERMOMETER,
        ),
        cv.Optional(CONF_BAUD_RATE): select.select_schema(
            BaudRateSelect,
            entity_category=ENTITY_CATEGORY_CONFIG,
            icon=ICON_THERMOMETER,
        ),
    }
)


async def to_code(config):
    as201_component = await cg.get_variable(config[CONF_AS201_ID])

    if direction_config := config.get(CONF_DIRECTION):
        s = await select.new_select(
            direction_config,
            options=[
                "vertical",
                "horizontal",
            ],
        )
        await cg.register_parented(s, config[CONF_AS201_ID])
        cg.add(as201_component.set_direction_select(s))
    if upload_rate_config := config.get(CONF_UPLOAD_RATE):
        s = await select.new_select(
            upload_rate_config,
            options=[
                "0.1Hz",
                "0.5Hz",
                "1Hz",
                "2Hz",
                "5Hz",
                "10Hz",
                "20Hz"
            ],
        )
        await cg.register_parented(s, config[CONF_AS201_ID])
        cg.add(as201_component.set_upload_rate_select(s))
    if baud_rate_config := config.get(CONF_BAUD_RATE):
        s = await select.new_select(
            baud_rate_config,
            options=[
                "4800",
                "9600",
                "19200",
                "38400",
                "57600",
                "115200",
                "230400",
                "460800",
                "500000",
                "921600"
            ],
        )
        await cg.register_parented(s, config[CONF_AS201_ID])
        cg.add(as201_component.set_baud_rate_select(s))
