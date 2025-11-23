#include "sensitivity_select.h"

namespace esphome {
namespace ld2460 {

void SensitivitySelect::control(const std::string &value) {
  this->publish_state(value);
  this->parent_->set_sensitivity(this->current_option());
  this->parent_->get_sensitivity();
}

}  // namespace ld2460
}  // namespace esphome
