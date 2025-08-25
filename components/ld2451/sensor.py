import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import UNIT_METER, CONF_SPEED, UNIT_KILOMETER_PER_HOUR, ICON_SIGNAL, STATE_CLASS_MEASUREMENT
from esphome.components import sensor
from esphome.const import (
    CONF_TARGET,
    CONF_DISTANCE,
    DEVICE_CLASS_DISTANCE, UNIT_DEGREES, DEVICE_CLASS_SPEED, CONF_ANGLE, CONF_SIGNAL_STRENGTH
)
from . import CONF_LD2451_ID, LD2451Component, MAX_TARGETS

ICON_FORMAT_TEXT_ROTATION_ANGLE_UP = "mdi:format-text-rotation-angle-up"
ICON_MAP_MARKER_DISTANCE = "mdi:map-marker-distance"
ICON_SPEED = "mdi:speedometer"
ICON_CAR = "mdi:car-convertible"
CONF_TARGET_NUMBER = "target_number"

DEPENDENCIES = ["ld2451"]

CONFIG_SCHEMA = cv.All(
    cv.Schema(
        {
            cv.GenerateID(CONF_LD2451_ID): cv.use_id(LD2451Component),
            cv.Optional(CONF_TARGET_NUMBER): sensor.sensor_schema(
                icon=ICON_CAR,
                accuracy_decimals=0,
                state_class=STATE_CLASS_MEASUREMENT,
                unit_of_measurement="#",
                filters=[
                    {
                        "timeout": {
                            "timeout": cv.TimePeriod(milliseconds=1000),
                        }
                    },
                ],
            )
        }
    )
    .extend(
        {
            cv.Optional(f"{CONF_TARGET}_{n + 1}"): cv.Schema({
                cv.Optional(CONF_ANGLE): sensor.sensor_schema(unit_of_measurement=UNIT_DEGREES,
                                                              icon=ICON_FORMAT_TEXT_ROTATION_ANGLE_UP,
                                                              filters=[
                                                                  {
                                                                      "timeout": {
                                                                          "timeout": cv.TimePeriod(milliseconds=1000),
                                                                      }
                                                                  },
                                                              ], ),
                cv.Optional(CONF_DISTANCE): sensor.sensor_schema(device_class=DEVICE_CLASS_DISTANCE,
                                                                 unit_of_measurement=UNIT_METER,
                                                                 icon=ICON_MAP_MARKER_DISTANCE,
                                                                 filters=[
                                                                     {
                                                                         "timeout": {
                                                                             "timeout": cv.TimePeriod(
                                                                                 milliseconds=1000),
                                                                         }
                                                                     },
                                                                 ], ),
                cv.Optional(CONF_SPEED): sensor.sensor_schema(device_class=DEVICE_CLASS_SPEED,
                                                              unit_of_measurement=UNIT_KILOMETER_PER_HOUR,
                                                              icon=ICON_SPEED,
                                                              filters=[
                                                                  {
                                                                      "timeout": {
                                                                          "timeout": cv.TimePeriod(milliseconds=1000),
                                                                      }
                                                                  },
                                                              ], ),
                cv.Optional(CONF_SIGNAL_STRENGTH): sensor.sensor_schema(unit_of_measurement="#",
                                                                        icon=ICON_SIGNAL,
                                                                        filters=[
                                                                            {
                                                                                "timeout": {
                                                                                    "timeout": cv.TimePeriod(
                                                                                        milliseconds=1000),
                                                                                }
                                                                            },
                                                                        ], )  # 信噪比

            }) for n in range(MAX_TARGETS)
        }
    )
)


async def to_code(config):
    ld2451_component = await cg.get_variable(config[CONF_LD2451_ID])
    if target_number_config := config.get(CONF_TARGET_NUMBER):
        sens = await sensor.new_sensor(target_number_config)
        cg.add(ld2451_component.set_target_number_sensor(sens))
    for n in range(MAX_TARGETS):
        if target_conf := config.get(f"{CONF_TARGET}_{n + 1}"):
            if angle_conf := target_conf.get(CONF_ANGLE):
                sens = await sensor.new_sensor(angle_conf)
                cg.add(ld2451_component.set_target_angle_sensor(n, sens))
                # cg.add(getattr(ld2451_component, f"set_target{n + 1}_angle_sensor")(sens))
            if distance_conf := target_conf.get(CONF_DISTANCE):
                sens = await sensor.new_sensor(distance_conf)
                cg.add(ld2451_component.set_target_distance_sensor(n, sens))
                # cg.add(getattr(ld2451_component, f"set_target{n + 1}_distance_sensor")(sens))
            if speed_conf := target_conf.get(CONF_SPEED):
                sens = await sensor.new_sensor(speed_conf)
                cg.add(ld2451_component.set_target_speed_sensor(n, sens))
                # cg.add(getattr(ld2451_component, f"set_target{n + 1}_speed_sensor")(sens))
            if signal_strength_conf := target_conf.get(CONF_SIGNAL_STRENGTH):
                sens = await sensor.new_sensor(signal_strength_conf)
                cg.add(ld2451_component.set_target_signal_strength_sensor(n, sens))
                # cg.add(getattr(ld2451_component, f"set_target{n + 1}_signal_strength_sensor")(sens))
