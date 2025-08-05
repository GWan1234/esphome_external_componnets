#include "acd4100.h"
#include "esphome/components/i2c/i2c.h"
#include "esphome/core/hal.h"
#include "esphome/core/log.h"

namespace esphome {
namespace acd4100 {

static const char *const TAG = "acd4100";
static const uint8_t READ_CMD[2] = {0x03, 0x00};  // Read command

uint8_t acd4100_crc8(const uint8_t *dat, uint8_t size) {
  uint8_t crc = 0xFF, i;
  for (uint8_t b = 0; b < size; b++) {
    crc ^= (dat[b]);
    for (i = 0; i < 8; i++) {
      if (crc & 0x80) {
        crc = (crc << 1) ^ 0x31;
      } else {
        crc <<= 1;
      }
    }
  }
  return crc;
}

void ACD4100Component::setup() { ESP_LOGCONFIG(TAG, "Running setup"); }

void ACD4100Component::dump_config() {
  char buffer[11];
  char snbuff[11];
  buffer[10] = '\0';  // Ensure null-termination
  snbuff[10] = '\0';  // Ensure null-termination
  this->sn(snbuff);
  this->version(buffer);
  ESP_LOGCONFIG(TAG, "ACD4100:\n"
                "  Version: %s\nSN: %s\n", buffer, snbuff);
  LOG_I2C_DEVICE(this);
  LOG_SENSOR("  ", "R32 SENSOR", this->r32_sensor_);
  LOG_SENSOR("  ", "TEMPERATURE SENSOR", this->temperature_sensor_);
  LOG_SENSOR("  ", "CO2 BASE", this->base_sensor_);
}

void ACD4100Component::update() {
  this->write(READ_CMD, 2);
  uint8_t data[9];
  this->read(data, 9);
  uint8_t crc = acd4100_crc8(data, 2);
  if (crc != data[2]) {
    ESP_LOGW(TAG, "ACD4100 CRC error: expected %02X, got %02X", crc, data[2]);
    return;  // CRC error
  }
  crc = acd4100_crc8((uint8_t *) data + 3, 2);
  if (crc != data[5]) {
    ESP_LOGW(TAG, "ACD4100 CRC error: expected %02X, got %02X", crc, data[5]);
    return;  // CRC error
  }
  crc = acd4100_crc8((uint8_t *) data + 6, 2);
  if (crc != data[8]) {
    ESP_LOGW(TAG, "ACD4100 CRC error: expected %02X, got %02X", crc, data[8]);
    return;  // CRC error
  }
  if (this->r32_sensor_ != nullptr) {
    uint32_t r32 = ((uint32_t) data[0]) << 24 | ((uint32_t) data[1]) << 16 | ((uint32_t) data[3]) << 8 |
                   ((uint32_t) data[4]);  // 解析CO2浓度数据
    this->r32_sensor_->publish_state(r32);
  }
  if (this->temperature_sensor_ != nullptr) {
    int16_t temperature = ((int16_t) data[6]) << 8 | ((int16_t) data[7]);  // 解析温度数据
    this->temperature_sensor_->publish_state(temperature);                 // 温度单位转换为摄氏度
  }
  if (this->base_sensor_ != nullptr) {
     uint16_t base = this->read_base();          // 基准值单位转换为ppm
     this->base_sensor_->publish_state(base);
  }
}

void ACD4100Component::set_calibrate_mode(bool auto_) {
  uint8_t chr;
  if(auto_) {
    chr=0x01;  // 自动校准
  }else {
    chr=0x00;  // 手动校准
  }
  uint8_t buffer[5] = {0x53, 0x06, 0x00, chr, 0x00};
  buffer[4] = acd4100_crc8(buffer, 4);  // 计算CRC
  this->write(buffer, 5);               // 写入校准数据
}

bool ACD4100Component::get_calibrate_mode() {
  uint8_t data[3] = {0x53, 0x06, 0x00};  // 读取校准数据命令
  this->write(data, 2);
  this->read(data, 3);
  uint8_t crc = acd4100_crc8(data, 2);
  if (crc != data[2]) {
    ESP_LOGW(TAG, "ACD4100 CRC error: expected %02X, got %02X", crc, data[2]);
    return 0;
  }
  bool auto_;
  if(data[1]) {
    auto_=true;  // 自动校准
  } else {
    auto_=false;  // 手动校准
  }
  return auto_;
}

void ACD4100Component::calibrate(uint16_t data) {
  uint8_t buffer[5] = {0x52, 0x04, (uint8_t) (data >> 8), (uint8_t) (data & 0xFF), 0x00};
  buffer[4] = acd4100_crc8(buffer, 4);  // 计算CRC
  this->write(buffer, 5);               // 写入校准数据
}

uint16_t ACD4100Component::read_base() {
  uint8_t data[3] = {0x52, 0x04, 0x00};  // 读取校准数据命令
  this->write(data, 2);
  this->read(data, 3);
  uint8_t crc = acd4100_crc8(data, 2);
  if (crc != data[2]) {
    ESP_LOGW(TAG, "ACD4100 CRC error: expected %02X, got %02X", crc, data[2]);
    return 0;
  }
  uint16_t calibration_value = ((uint16_t) data[0]) << 8 | ((uint16_t) data[1]);  // 解析校准值
  return calibration_value;
}

void ACD4100Component::reset() {
  uint8_t reset_cmd[3] = {0x52, 0x02, 0x00};  // 重置命令
  this->write(reset_cmd, 3);
  this->write(reset_cmd, 2);                  // 写入重置命令
  this->read(reset_cmd, 3);                   // 读取响应
  uint8_t crc = acd4100_crc8(reset_cmd, 2);
  if (crc != reset_cmd[2]) {
    ESP_LOGW(TAG, "ACD4100 reset CRC error: expected %02X, got %02X", crc, reset_cmd[2]);
    return;  // CRC error
  }
  if(reset_cmd[1]!=0x01){
    ESP_LOGW(TAG, "ACD4100 reset failed: expected 0x01, got %02X", reset_cmd[1]);
    return;  // Reset failed
  }
}

void ACD4100Component::version(char *buffer) {
  uint8_t data[2] = {0xD1, 0x00};  // 版本查询命令
  this->write(data, 2);                  // 写入版本查询命令
  this->read((uint8_t*)buffer, 10);                  // 读取响应
}

void ACD4100Component::sn(char *buffer) {
  uint8_t data[2] = {0xD2, 0x01};  // 编号查询命令
  this->write(data, 2);                  // 写入命令
  this->read((uint8_t*)buffer, 10);                  // 读取响应
}

}  // namespace acd4100
}  // namespace esphome