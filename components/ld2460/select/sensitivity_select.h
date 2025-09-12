#pragma once

#include "esphome/components/select/select.h"
#include "../ld2460.h"

namespace esphome {
namespace ld2460 {

class SensitivitySelect : public select::Select, public Parented<LD2460Component> {
 public:
  SensitivitySelect() = default;

 protected:
  void control(const std::string &value) override;
};

}  // namespace ld2460
}  // namespace esphome
