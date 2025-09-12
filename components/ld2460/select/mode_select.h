#pragma once

#include "esphome/components/select/select.h"
#include "../ld2460.h"

namespace esphome {
namespace ld2460 {

class ModeSelect : public select::Select, public Parented<LD2460Component> {
 public:
  ModeSelect() = default;

 protected:
  void control(const std::string &value) override;
};

}  // namespace ld2460
}  // namespace esphome
