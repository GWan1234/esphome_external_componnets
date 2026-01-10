import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor
from esphome.const import (
    DEVICE_CLASS_MOTION,
)

from . import CONF_ML307R_ID, ML307RComponent

CONF_ONLINE = "online"

DEPENDENCIES = ["ml307r"]

CONFIG_SCHEMA = cv.All(
    cv.Schema(
        {
            cv.GenerateID(CONF_ML307R_ID): cv.use_id(ML307RComponent),
            cv.Optional(CONF_ONLINE): binary_sensor.binary_sensor_schema(device_class=DEVICE_CLASS_MOTION,),
        }
    )
)

async def to_code(config):
    ml307r_component = await cg.get_variable(config[CONF_ML307R_ID])

    if CONF_ONLINE in config:
        sens = await binary_sensor.new_binary_sensor(config[CONF_ONLINE])
        cg.add(ml307r_component.set_online_binary_sensor(sens))