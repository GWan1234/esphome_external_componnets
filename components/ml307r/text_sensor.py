import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import text_sensor
from esphome.const import (
    ICON_CHIP, CONF_VERSION
)

from . import CONF_ML307R_ID, ML307RComponent

DEPENDENCIES = ["ml307r"]

CONF_SMS_SENDER = "sms_sender"
CONF_SMS_CONTENT = "sms_content"
CONF_SMS_TIMESTAMP = "sms_timestamp"
CONF_NETWORK_STATUS = "network_status"

CONFIG_SCHEMA = cv.All(
    cv.Schema(
        {
            cv.GenerateID(CONF_ML307R_ID): cv.use_id(ML307RComponent),
            cv.Optional(CONF_SMS_SENDER): text_sensor.text_sensor_schema(
                icon=ICON_CHIP, ),
            cv.Optional(CONF_SMS_CONTENT): text_sensor.text_sensor_schema(
                icon=ICON_CHIP, ),
            cv.Optional(CONF_SMS_TIMESTAMP): text_sensor.text_sensor_schema(
                icon=ICON_CHIP, ),
            cv.Optional(CONF_NETWORK_STATUS): text_sensor.text_sensor_schema(
                icon=ICON_CHIP, ),
        }
    )
)


async def to_code(config):
    ml307r_component = await cg.get_variable(config[CONF_ML307R_ID])

    if CONF_SMS_SENDER in config:
        sens = await text_sensor.new_text_sensor(config[CONF_SMS_SENDER])
        cg.add(ml307r_component.set_sms_sender_text_sensor(sens))

    if CONF_SMS_CONTENT in config:
        sens = await text_sensor.new_text_sensor(config[CONF_SMS_CONTENT])
        cg.add(ml307r_component.set_sms_content_text_sensor(sens))

    if CONF_SMS_TIMESTAMP in config:
        sens = await text_sensor.new_text_sensor(config[CONF_SMS_TIMESTAMP])
        cg.add(ml307r_component.set_sms_timestamp_text_sensor(sens))

    if CONF_NETWORK_STATUS in config:
        sens = await text_sensor.new_text_sensor(config[CONF_NETWORK_STATUS])
        cg.add(ml307r_component.set_network_status_text_sensor(sens))

    if CONF_VERSION in config:
        sens = await text_sensor.new_text_sensor(config[CONF_VERSION])
        cg.add(ml307r_component.set_version_text_sensor(sens))
