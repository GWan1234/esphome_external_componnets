#include "height_number.h"

namespace esphome {
namespace ld2460 {

void HeightNumber::control(float value) {
  this->publish_state(value);
  this->parent_->set_install_params(value, this->parent_->angle_number_->state);
  this->parent_->get_install_params();
}

}  // namespace ld2460
}  // namespace esphome
