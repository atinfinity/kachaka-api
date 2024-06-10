# This file generated by tools/update_kachaka_api_base.py
# Don't edit directly

#  Copyright 2023 Preferred Robotics, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Iterator, TypedDict

import grpc
from google._upb._message import RepeatedCompositeContainer

from .generated import kachaka_api_pb2 as pb2
from .generated.kachaka_api_pb2_grpc import KachakaApiStub
from .util.layout import ShelfLocationResolver

MAX_LINEAR_VELOCITY = 0.3
MAX_ANGULAR_VELOCITY = 1.57


class KachakaApiClientBase:
    def __init__(self, target: str = "100.94.1.1:26400"):
        self.stub = KachakaApiStub(grpc.insecure_channel(target))
        self.resolver = ShelfLocationResolver()

    def get_robot_serial_number(self) -> str:
        request = pb2.GetRequest()
        response: pb2.GetRobotSerialNumberResponse = (
            self.stub.GetRobotSerialNumber(request)
        )
        return response.serial_number

    def get_robot_version(self) -> str:
        request = pb2.GetRequest()
        response: pb2.GetRobotVersionResponse = self.stub.GetRobotVersion(
            request
        )
        return response.version

    def get_robot_pose(self) -> pb2.Pose:
        request = pb2.GetRequest()
        response: pb2.GetRobotPoseResponse = self.stub.GetRobotPose(request)
        return response.pose

    def get_battery_info(self) -> tuple[float, pb2.PowerSupplyStatus]:
        request = pb2.GetRequest()
        response: pb2.GetBatteryInfoResponse = self.stub.GetBatteryInfo(request)
        return response.remaining_percentage, response.power_supply_status

    def get_png_map(self) -> pb2.Map:
        request = pb2.GetRequest()
        response: pb2.GetPngMapResponse = self.stub.GetPngMap(request)
        return response.map

    def get_object_detection(
        self,
    ) -> tuple[pb2.RosHeader, RepeatedCompositeContainer]:
        request = pb2.GetRequest()
        response: pb2.GetObjectDetectionResponse = self.stub.GetObjectDetection(
            request
        )
        return (response.header, response.objects)

    def get_object_detection_features(
        self,
    ) -> tuple[pb2.RosHeader, RepeatedCompositeContainer]:
        request = pb2.GetRequest()
        response: pb2.GetObjectDetectionFeaturesResponse = (
            self.stub.GetObjectDetectionFeatures(request)
        )
        return (response.header, response.features)

    def get_ros_imu(self) -> pb2.RosImu:
        request = pb2.GetRequest()
        response: pb2.GetRosImuResponse = self.stub.GetRosImu(request)
        return response.imu

    def get_ros_odometry(self) -> pb2.RosOdometry:
        request = pb2.GetRequest()
        response: pb2.GetRosOdometryResponse = self.stub.GetRosOdometry(request)
        return response.odometry

    def get_ros_laser_scan(self) -> pb2.RosLaserScan:
        request = pb2.GetRequest()
        response: pb2.GetRosLaserScanResponse = self.stub.GetRosLaserScan(
            request
        )
        return response.scan

    def get_front_camera_ros_camera_info(self) -> pb2.RosCameraInfo:
        request = pb2.GetRequest()
        response: pb2.GetFrontCameraRosCameraInfoResponse = (
            self.stub.GetFrontCameraRosCameraInfo(request)
        )
        return response.camera_info

    def get_front_camera_ros_image(self) -> pb2.RosImage:
        request = pb2.GetRequest()
        response: pb2.GetFrontCameraRosImageResponse = (
            self.stub.GetFrontCameraRosImage(request)
        )
        return response.image

    def get_front_camera_ros_compressed_image(
        self,
    ) -> pb2.RosCompressedImage:
        request = pb2.GetRequest()
        response: pb2.GetFrontCameraRosCompressedImageResponse = (
            self.stub.GetFrontCameraRosCompressedImage(request)
        )
        return response.image

    def get_back_camera_ros_camera_info(self) -> pb2.RosCameraInfo:
        request = pb2.GetRequest()
        response: pb2.GetBackCameraRosCameraInfoResponse = (
            self.stub.GetBackCameraRosCameraInfo(request)
        )
        return response.camera_info

    def get_back_camera_ros_image(self) -> pb2.RosImage:
        request = pb2.GetRequest()
        response: pb2.GetBackCameraRosImageResponse = (
            self.stub.GetBackCameraRosImage(request)
        )
        return response.image

    def get_back_camera_ros_compressed_image(
        self,
    ) -> pb2.RosCompressedImage:
        request = pb2.GetRequest()
        response: pb2.GetBackCameraRosCompressedImageResponse = (
            self.stub.GetBackCameraRosCompressedImage(request)
        )
        return response.image

    def get_tof_camera_ros_camera_info(self) -> pb2.RosCameraInfo:
        request = pb2.GetRequest()
        response: pb2.GetTofCameraRosCameraInfoResponse = (
            self.stub.GetTofCameraRosCameraInfo(request)
        )
        return response.camera_info

    def get_tof_camera_ros_image(self) -> pb2.RosImage:
        request = pb2.GetRequest()
        response: pb2.GetTofCameraRosImageResponse = (
            self.stub.GetTofCameraRosImage(request)
        )
        if not response.is_available:
            raise Exception("tof is not available on charger.")
        return response.image

    def get_tof_camera_ros_compressed_image(
        self,
    ) -> pb2.RosCompressedImage:
        request = pb2.GetRequest()
        response: pb2.GetTofCameraRosCompressedImageResponse = (
            self.stub.GetTofCameraRosCompressedImage(request)
        )
        if not response.is_available:
            raise Exception("tof is not available on charger.")
        return response.image

    def start_command(
        self,
        command: pb2.Command,
        *,
        wait_for_completion: bool = True,
        cancel_all: bool = True,
        tts_on_success: str = "",
        title: str = "",
    ) -> pb2.Result:
        request = pb2.StartCommandRequest(
            command=command,
            cancel_all=cancel_all,
            tts_on_success=tts_on_success,
            title=title,
        )
        # Get the cursor position before start_command
        command_state_metadata = pb2.Metadata(cursor=0)
        command_state_metadata.cursor = (
            self.stub.GetCommandState(
                pb2.GetRequest(metadata=command_state_metadata)
            )
        ).metadata.cursor
        response: pb2.StartCommandResponse = self.stub.StartCommand(request)
        if not response.result.success or not wait_for_completion:
            return response.result
        while True:
            command_result_response: pb2.GetLastCommandResultResponse = (
                self.stub.GetLastCommandResult(
                    pb2.GetRequest(metadata=command_state_metadata)
                )
            )
            command_state_metadata.cursor = (
                command_result_response.metadata.cursor
            )
            if command_result_response.command_id == response.command_id:
                break
        return (self.get_last_command_result())[0]

    def move_shelf(
        self,
        shelf_name_or_id: str,
        location_name_or_id: str,
        *,
        wait_for_completion: bool = True,
        cancel_all: bool = True,
        tts_on_success: str = "",
        title: str = "",
    ) -> pb2.Result:
        shelf_id = self.resolver.get_shelf_id_by_name(shelf_name_or_id)
        location_id = self.resolver.get_location_id_by_name(location_name_or_id)
        return self.start_command(
            pb2.Command(
                move_shelf_command=pb2.MoveShelfCommand(
                    target_shelf_id=shelf_id,
                    destination_location_id=location_id,
                )
            ),
            wait_for_completion=wait_for_completion,
            cancel_all=cancel_all,
            tts_on_success=tts_on_success,
            title=title,
        )

    def return_shelf(
        self,
        shelf_name_or_id: str = "",
        *,
        wait_for_completion: bool = True,
        cancel_all: bool = True,
        tts_on_success: str = "",
        title: str = "",
    ) -> pb2.Result:
        shelf_id = self.resolver.get_shelf_id_by_name(shelf_name_or_id)
        return self.start_command(
            pb2.Command(
                return_shelf_command=pb2.ReturnShelfCommand(
                    target_shelf_id=shelf_id
                )
            ),
            wait_for_completion=wait_for_completion,
            cancel_all=cancel_all,
            tts_on_success=tts_on_success,
            title=title,
        )

    def undock_shelf(
        self,
        *,
        wait_for_completion: bool = True,
        cancel_all: bool = True,
        tts_on_success: str = "",
        title: str = "",
    ) -> pb2.Result:
        return self.start_command(
            pb2.Command(undock_shelf_command=pb2.UndockShelfCommand()),
            wait_for_completion=wait_for_completion,
            cancel_all=cancel_all,
            tts_on_success=tts_on_success,
            title=title,
        )

    def move_to_location(
        self,
        location_name_or_id: str,
        *,
        wait_for_completion: bool = True,
        cancel_all: bool = True,
        tts_on_success: str = "",
        title: str = "",
    ) -> pb2.Result:
        location_id = self.resolver.get_location_id_by_name(location_name_or_id)
        return self.start_command(
            pb2.Command(
                move_to_location_command=pb2.MoveToLocationCommand(
                    target_location_id=location_id
                )
            ),
            wait_for_completion=wait_for_completion,
            cancel_all=cancel_all,
            tts_on_success=tts_on_success,
            title=title,
        )

    def return_home(
        self,
        *,
        wait_for_completion: bool = True,
        cancel_all: bool = True,
        tts_on_success: str = "",
        title: str = "",
    ) -> pb2.Result:
        return self.start_command(
            pb2.Command(return_home_command=pb2.ReturnHomeCommand()),
            wait_for_completion=wait_for_completion,
            cancel_all=cancel_all,
            tts_on_success=tts_on_success,
            title=title,
        )

    def dock_shelf(
        self,
        *,
        wait_for_completion: bool = True,
        cancel_all: bool = True,
        tts_on_success: str = "",
        title: str = "",
    ) -> pb2.Result:
        return self.start_command(
            pb2.Command(dock_shelf_command=pb2.DockShelfCommand()),
            wait_for_completion=wait_for_completion,
            cancel_all=cancel_all,
            tts_on_success=tts_on_success,
            title=title,
        )

    def speak(
        self,
        text: str,
        *,
        wait_for_completion: bool = True,
        cancel_all: bool = True,
        tts_on_success: str = "",
        title: str = "",
    ) -> pb2.Result:
        return self.start_command(
            pb2.Command(speak_command=pb2.SpeakCommand(text=text)),
            wait_for_completion=wait_for_completion,
            cancel_all=cancel_all,
            tts_on_success=tts_on_success,
            title=title,
        )

    def move_to_pose(
        self,
        x: float,
        y: float,
        yaw: float,
        *,
        wait_for_completion: bool = True,
        cancel_all: bool = True,
        tts_on_success: str = "",
        title: str = "",
    ) -> pb2.Result:
        return self.start_command(
            pb2.Command(
                move_to_pose_command=pb2.MoveToPoseCommand(x=x, y=y, yaw=yaw)
            ),
            wait_for_completion=wait_for_completion,
            cancel_all=cancel_all,
            tts_on_success=tts_on_success,
            title=title,
        )

    def cancel_command(self) -> tuple[pb2.Result, pb2.Command]:
        request = pb2.EmptyRequest()
        response: pb2.CancelCommandResponse = self.stub.CancelCommand(request)
        return (response.result, response.command)

    def get_command_state(self) -> tuple[pb2.CommandState, pb2.Command]:
        request = pb2.GetRequest()
        response: pb2.GetCommandStateResponse = self.stub.GetCommandState(
            request
        )
        return (response.state, response.command)

    def is_command_running(self) -> bool:
        request = pb2.GetRequest()
        response: pb2.GetCommandStateResponse = self.stub.GetCommandState(
            request
        )
        return response.state == pb2.CommandState.COMMAND_STATE_RUNNING

    def get_running_command(self) -> pb2.Command | None:
        request = pb2.GetRequest()
        response: pb2.GetCommandStateResponse = self.stub.GetCommandState(
            request
        )
        return response.command if response.HasField("command") else None

    def get_last_command_result(self) -> tuple[pb2.Result, pb2.Command]:
        request = pb2.GetRequest()
        response: pb2.GetLastCommandResultResponse = (
            self.stub.GetLastCommandResult(request)
        )
        return (response.result, response.command)

    def get_locations(
        self,
    ) -> RepeatedCompositeContainer:
        request = pb2.GetRequest()
        response: pb2.GetLocationsResponse = self.stub.GetLocations(request)
        return response.locations

    def get_default_location_id(self) -> str:
        request = pb2.GetRequest()
        response: pb2.GetLocationsResponse = self.stub.GetLocations(request)
        return response.default_location_id

    def get_shelves(
        self,
    ) -> RepeatedCompositeContainer:
        request = pb2.GetRequest()
        response: pb2.GetShelvesResponse = self.stub.GetShelves(request)
        return response.shelves

    def get_moving_shelf_id(self) -> str:
        request = pb2.GetRequest()
        response: pb2.GetMovingShelfIdResponse = self.stub.GetMovingShelfId(
            request
        )
        return response.shelf_id

    def reset_shelf_pose(self, shelf_id: str) -> pb2.Result:
        request = pb2.ResetShelfPoseRequest(shelf_id=shelf_id)
        response: pb2.ResetShelfPoseResponse = self.stub.ResetShelfPose(request)
        return response.result

    def set_auto_homing_enabled(self, enable: bool) -> pb2.Result:
        request = pb2.SetAutoHomingEnabledRequest(enable=enable)
        response: pb2.SetAutoHomingEnabledResponse = (
            self.stub.SetAutoHomingEnabled(request)
        )
        return response.result

    def get_auto_homing_enabled(self) -> bool:
        request = pb2.GetRequest()
        response: pb2.GetAutoHomingEnabledResponse = (
            self.stub.GetAutoHomingEnabled(request)
        )
        return response.enabled

    def set_manual_control_enabled(self, enable: bool) -> pb2.Result:
        request = pb2.SetManualControlEnabledRequest(enable=enable)
        response: pb2.SetManualControlEnabledResponse = (
            self.stub.SetManualControlEnabled(request)
        )
        return response.result

    def get_manual_control_enabled(self) -> bool:
        request = pb2.GetRequest()
        response: pb2.GetManualControlEnabledResponse = (
            self.stub.GetManualControlEnabled(request)
        )
        return response.enabled

    def _impl_set_robot_velocity(
        self, linear: float, angular: float
    ) -> pb2.Result:
        request = pb2.SetRobotVelocityRequest(
            linear=linear / MAX_LINEAR_VELOCITY,
            angular=angular / MAX_ANGULAR_VELOCITY,
        )
        response: pb2.SetRobotVelocityResponse = self.stub.SetRobotVelocity(
            request
        )
        return response.result

    def set_robot_velocity(self, linear: float, angular: float) -> pb2.Result:
        result = self._impl_set_robot_velocity(linear, angular)
        if result.success:
            return result
        self.set_manual_control_enabled(True)
        return self._impl_set_robot_velocity(linear, angular)

    def set_robot_stop(self):
        self.set_robot_velocity(0, 0)
        self.set_manual_control_enabled(False)

    def get_map_list(self) -> RepeatedCompositeContainer:
        request = pb2.GetRequest()
        response: pb2.GetMapListResponse = self.stub.GetMapList(request)
        return response.map_list_entries

    def get_current_map_id(self) -> str:
        request = pb2.GetRequest()
        response: pb2.GetCurrentMapIdResponse = self.stub.GetCurrentMapId(
            request
        )
        return response.id

    def load_map_preview(self, map_id: str) -> tuple[pb2.Result, pb2.Map]:
        request = pb2.LoadMapPreviewRequest(map_id=map_id)
        response: pb2.LoadMapPreviewResponse = self.stub.LoadMapPreview(request)
        return response.map

    def export_map(self, map_id: str, output_file_path: str) -> pb2.Result:
        request = pb2.ExportMapRequest(map_id=map_id)
        responses: Iterator[pb2.ExportMapResponse] = self.stub.ExportMap(
            request
        )
        data = bytes()
        result = pb2.Result(success=False)
        for response in responses:
            if response.HasField("middle_of_stream"):
                data += response.middle_of_stream.data
            elif response.HasField("end_of_stream"):
                result = response.end_of_stream.result

        if not result.success:
            return result

        with open(output_file_path, "wb") as file:
            file.write(data)
        return result

    def import_map(
        self, target_file_path: str, chunk_size: int = 1024 * 1024
    ) -> tuple[pb2.Result, str]:
        def request_iterator() -> Iterator[pb2.ImportMapRequest]:
            with open(target_file_path, mode="rb") as file:
                while True:
                    chunk: bytes = file.read(chunk_size)
                    if not chunk:
                        break
                    yield pb2.ImportMapRequest(data=chunk)

        response: pb2.ImportMapResponse = self.stub.ImportMap(
            request_iterator()
        )
        return response.result, response.map_id

    class Pose2d(TypedDict):
        x: float
        y: float
        theta: float

    def switch_map(
        self, map_id: str, *, pose: Pose2d | None = None
    ) -> pb2.Result:
        # If "pose" is not specified, the initial pose is automatically determined based on
        # the mapping mode used for the target map.
        # In the narrow mode (~200㎡), the initial pose becomes the charger pose.
        # In the wide mode (200㎡~), the initial pose becomes the same pose before switching.
        # In a future release, the automatically determined initial pose will be the charger pose.
        initial_pose = (
            pb2.Pose(x=pose["x"], y=pose["y"], theta=pose["theta"])
            if pose
            else None
        )
        request = pb2.SwitchMapRequest(map_id=map_id, initial_pose=initial_pose)
        response: pb2.SwitchMapResponse = self.stub.SwitchMap(request)
        return response.result

    def get_history_list(
        self,
    ) -> RepeatedCompositeContainer:
        request = pb2.GetRequest()
        response: pb2.GetHistoryListResponse = self.stub.GetHistoryList(request)
        return response.histories

    def update_resolver(self) -> None:
        self.resolver.set_shelves(self.get_shelves())
        self.resolver.set_locations(self.get_locations())
