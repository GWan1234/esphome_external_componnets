#include "baud_rate_select.h"

namespace esphome {
namespace ld2460 {

void BaudRateSelect::control(const std::string &value) {
  this->publish_state(value);
  this->parent_->set_baud_rate(state);
}

}  // namespace ld2460
}  // namespace esphome
