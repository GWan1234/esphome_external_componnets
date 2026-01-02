#include "baud_rate_select.h"

namespace esphome {
namespace as201 {

void BaudRateSelect::control(const std::string &value) {
  this->publish_state(value);
  this->parent_->set_baud_rate(this->current_option());
}

}  // namespace as201
}  // namespace esphome
