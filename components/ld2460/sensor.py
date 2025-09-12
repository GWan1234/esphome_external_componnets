import esphome.codegen as cg
from esphome.components import sensor
import esphome.config_validation as cv
from esphome.const import (
    CONF_ID,
    ICON_ACCOUNT,
    CONF_X, CONF_Y, STATE_CLASS_MEASUREMENT, DEVICE_CLASS_DISTANCE, UNIT_METER, ICON_PULSE,
    ICON_HEART_PULSE, UNIT_BEATS_PER_MINUTE
)

from . import CONF_LD2460_ID, LD2460Component, MAX_TARGETS

DEPENDENCIES = ["ld2460"]

CONF_TARGET_NUMBER = "target_number"
CONF_TARGET = "target"
ICON_ALPHA_X_BOX_OUTLINE = "mdi:alpha-x-box-outline"
ICON_ALPHA_Y_BOX_OUTLINE = "mdi:alpha-y-box-outline"

CONFIG_SCHEMA = cv.All(
    cv.Schema(
        {
            cv.GenerateID(CONF_LD2460_ID): cv.use_id(LD2460Component),
            cv.Optional(CONF_TARGET_NUMBER): sensor.sensor_schema(
                icon=ICON_ACCOUNT,
                accuracy_decimals=0,
                state_class=STATE_CLASS_MEASUREMENT,
                filters=[
                    {
                        "timeout": {
                            "timeout": cv.TimePeriod(milliseconds=1000),
                            "value": 0,
                        }
                    },
                ],
            ),
        }
    ).extend(
        {
            cv.Optional(f"{CONF_TARGET}_{n + 1}"): cv.Schema({
                cv.Optional(CONF_X): sensor.sensor_schema(device_class=DEVICE_CLASS_DISTANCE,
                                                          icon=ICON_ALPHA_X_BOX_OUTLINE,
                                                          unit_of_measurement=UNIT_METER,
                                                          accuracy_decimals=1,
                                                          filters=[
                                                              {
                                                                  "timeout": {
                                                                      "timeout": cv.TimePeriod(milliseconds=1000),
                                                                  }
                                                              },
                                                          ]),
                cv.Optional(CONF_Y): sensor.sensor_schema(device_class=DEVICE_CLASS_DISTANCE,
                                                          icon=ICON_ALPHA_Y_BOX_OUTLINE,
                                                          unit_of_measurement=UNIT_METER,
                                                          accuracy_decimals=1,
                                                          filters=[
                                                              {
                                                                  "timeout": {
                                                                      "timeout": cv.TimePeriod(milliseconds=1000),
                                                                  }
                                                              },
                                                          ]),
            })
            for n in range(MAX_TARGETS)
        }
    )
)

async def to_code(config):
    ld2460_component = await cg.get_variable(config[CONF_LD2460_ID])

    if target_number_config := config.get(CONF_TARGET_NUMBER):
        sens = await sensor.new_sensor(target_number_config)
        cg.add(ld2460_component.set_target_number_sensor(sens))

    for n in range(MAX_TARGETS):
        if target_config := config.get(f"{CONF_TARGET}_{n + 1}"):
            if conf := target_config.get(CONF_X):
                sens = await sensor.new_sensor(conf)
                cg.add(ld2460_component.set_target_x_sensor(n, sens))
            if conf := target_config.get(CONF_Y):
                sens = await sensor.new_sensor(conf)
                cg.add(ld2460_component.set_target_y_sensor(n, sens))