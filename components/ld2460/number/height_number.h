#pragma once

#include "esphome/components/number/number.h"
#include "../ld2460.h"

namespace esphome {
namespace ld2460 {

class HeightNumber : public number::Number, public Parented<LD2460Component> {
 public:
  HeightNumber() = default;

 protected:
  void control(float value) override;
};

} // namespace ld2460
} // namespace esphome