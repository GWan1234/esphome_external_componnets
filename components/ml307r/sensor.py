import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    DEVICE_CLASS_SIGNAL_STRENGTH,
    STATE_CLASS_MEASUREMENT,
    UNIT_DECIBEL_MILLIWATT,
)

from . import CONF_ML307R_ID, ML307RComponent

DEPENDENCIES = ["ml307r"]

CONF_SIGNAL_STRENGTH = "signal_strength"

CONFIG_SCHEMA = cv.All(
    cv.Schema(
        {
            cv.GenerateID(CONF_ML307R_ID): cv.use_id(ML307RComponent),
            cv.Optional(CONF_SIGNAL_STRENGTH): sensor.sensor_schema(
                unit_of_measurement=UNIT_DECIBEL_MILLIWATT,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_SIGNAL_STRENGTH,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
        }
    )
)

async def to_code(config):
    ml307r_component = await cg.get_variable(config[CONF_ML307R_ID])

    if CONF_SIGNAL_STRENGTH in config:
        sens = await sensor.new_sensor(config[CONF_SIGNAL_STRENGTH])
        cg.add(ml307r_component.set_signal_strength_sensor(sens))