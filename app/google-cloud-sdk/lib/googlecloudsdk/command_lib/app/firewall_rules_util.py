# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Utilities for `gcloud app firewall-rules`."""

from googlecloudsdk.calliope import exceptions

# The default rule is placed at MaxInt32 - 1 and is always evaluated last
DEFAULT_RULE_PRIORITY = 2**31 - 1

LIST_FORMAT = """
  table(
    priority:sort=1,
    action,
    source_range,
    description
  )
  """


def ParseFirewallRule(registry, project, priority):
  """Creates a resource path given a firewall rule priority.

  Args:
    registry: str, the resource registry for this API version
    project: str, the cloud project name gcloud is operating on
    priority: str, the priority of the rule.

  Returns:
    The resource for the rule.

  """
  res = registry.Parse(
      str(ParsePriority(priority)),
      params={'appsId': project},
      collection='appengine.apps.firewall.ingressRules')
  return res


def ParsePriority(priority):
  """Converts a priority to an integer."""
  if priority == 'default':
    priority = DEFAULT_RULE_PRIORITY

  try:
    priority_int = int(priority)
    if priority_int <= 0 or priority_int > DEFAULT_RULE_PRIORITY:
      raise exceptions.InvalidArgumentException(
          'priority', 'Priority must be between 1 and {0} inclusive.'.format(
              DEFAULT_RULE_PRIORITY))
    return priority_int
  except ValueError:
    raise exceptions.InvalidArgumentException(
        'priority', 'Priority should be an integer value or `default`.')


def ParseAction(messages, action):
  """Converts an action string to the corresponding enum value.

  Options are: 'allow' or 'deny', otherwise None will be returned.

  Args:
    messages: apitools.base.protorpclite.messages, the proto messages class for
      this API version for firewall.
    action: str, the action as a string
  Returns:
    ActionValueValuesEnum type
  """
  if not action:
    return None
  return messages.FirewallRule.ActionValueValuesEnum(action.upper())


def RaiseMinArgument():
  raise exceptions.MinimumArgumentException([
      '--action', '--source-range', '--description'
  ], 'Please specify at least one attribute to the firewall-rules update.')
