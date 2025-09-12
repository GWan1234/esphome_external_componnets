#include "detect_distance_number.h"

namespace esphome {
namespace ld2460 {

void DetectDistanceNumber::control(float value) {
  this->publish_state(value);
  this->parent_->set_detect_range(this->parent_->detect_distance_number_->state,
                                  (int16_t) this->parent_->detect_start_angle_number_->state,
                                  (int16_t) this->parent_->detect_end_angle_number_->state);
  this->parent_->get_detect_range();
}

void DetectStartAngleNumber::control(float value) {
  this->publish_state(value);
  this->parent_->set_detect_range(this->parent_->detect_distance_number_->state,
                                  (int16_t) this->parent_->detect_start_angle_number_->state,
                                  (int16_t) this->parent_->detect_end_angle_number_->state);
  this->parent_->get_detect_range();
}

void DetectEndAngleNumber::control(float value) {
  this->publish_state(value);
  this->parent_->set_detect_range(this->parent_->detect_distance_number_->state,
                                  (int16_t) this->parent_->detect_start_angle_number_->state,
                                  (int16_t) this->parent_->detect_end_angle_number_->state);
  this->parent_->get_detect_range();
}

}  // namespace ld2460
}  // namespace esphome
