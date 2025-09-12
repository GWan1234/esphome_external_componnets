import esphome.codegen as cg
from esphome.components import binary_sensor
import esphome.config_validation as cv
from esphome.const import (
    CONF_TARGET, DEVICE_CLASS_MOTION
)

from . import CONF_LD2460_ID, LD2460Component

DEPENDENCIES = ["ld2460"]


CONFIG_SCHEMA = cv.All(
    cv.Schema(
        {
            cv.GenerateID(CONF_LD2460_ID): cv.use_id(LD2460Component),
            cv.Optional(CONF_TARGET): binary_sensor.binary_sensor_schema(
                device_class=DEVICE_CLASS_MOTION,
            )
        }
    )
)

async def to_code(config):
    ld2460_component = await cg.get_variable(config[CONF_LD2460_ID])

    if target_config := config.get(CONF_TARGET):
        sens = await binary_sensor.new_binary_sensor(target_config)
        cg.add(ld2460_component.set_target_binary_sensor(sens))