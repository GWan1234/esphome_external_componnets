import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_VERSION, ENTITY_CATEGORY_DIAGNOSTIC, ICON_CHIP, ICON_SIGN_DIRECTION, ENTITY_CATEGORY_NONE
from esphome.components import text_sensor

from esphome.const import CONF_DIRECTION, CONF_TARGET

from . import CONF_LD2451_ID, LD2451Component, MAX_TARGETS

DEPENDENCIES = ["ld2451"]

CONFIG_SCHEMA = cv.All(
    cv.Schema(
        {
            cv.GenerateID(CONF_LD2451_ID): cv.use_id(LD2451Component),
            cv.Optional(CONF_VERSION): text_sensor.text_sensor_schema(
                entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
                icon=ICON_CHIP,
            ),
        }
    ).extend(
        {
            cv.Optional(f"{CONF_TARGET}_{n + 1}"): cv.Schema({
                cv.Optional(CONF_DIRECTION): text_sensor.text_sensor_schema(
                    entity_category=ENTITY_CATEGORY_NONE,
                    icon=ICON_SIGN_DIRECTION,
                ),
            }) for n in range(MAX_TARGETS)
        }
    )
)


async def to_code(config):
    ld2451_component = await cg.get_variable(config[CONF_LD2451_ID])
    if version_config := config.get(CONF_VERSION):
        sens = await text_sensor.new_text_sensor(version_config)
        cg.add(ld2451_component.set_version_text_sensor(sens))
    for n in range(MAX_TARGETS):
        if target_conf := config.get(f"{CONF_TARGET}_{n + 1}"):
            if direction_conf := target_conf.get(CONF_DIRECTION):
                sens = await text_sensor.new_text_sensor(direction_conf)
                cg.add(ld2451_component.set_target_direction_text_sensor(n, sens))
                # cg.add(getattr(ld2451_component, f"set_target{n + 1}_direction_text_sensor")(sens))
