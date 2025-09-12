#include "angle_number.h"

namespace esphome {
namespace ld2460 {

void AngleNumber::control(float value) {
  this->publish_state(value);
  this->parent_->set_install_params(this->parent_->height_number_->state, value);
  this->parent_->get_install_params(); // todo read after change
}

}  // namespace ld2460
}  // namespace esphome
