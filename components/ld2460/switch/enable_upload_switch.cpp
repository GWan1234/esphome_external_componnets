#include "enable_upload_switch.h"

namespace esphome {
namespace ld2460 {

void EnableUploadSwitch::write_state(bool state) {
  this->publish_state(state);
  this->parent_->enable_upload(state);
}

}  // namespace ld2450
}  // namespace esphome
