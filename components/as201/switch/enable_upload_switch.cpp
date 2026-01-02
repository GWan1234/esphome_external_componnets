#include "enable_upload_switch.h"

namespace esphome {
namespace as201 {

void EnableUploadSwitch::write_state(bool state) {
  this->publish_state(state);
  this->parent_->enable_upload(state);
}

}  // namespace as201
}  // namespace esphome
