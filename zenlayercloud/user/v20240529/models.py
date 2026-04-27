#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.common.abstract_model import AbstractModel
import warnings

class DescribeMembersRequest(AbstractModel):
    def __init__(self):
        self.name = None
        self.username = None
        self.pageNum = None
        self.pageSize = None

    def _deserialize(self, params):
        self.name = params.get("name")
        self.username = params.get("username")
        self.pageNum = params.get("pageNum")
        self.pageSize = params.get("pageSize")


class DescribeMembersResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.totalCount = None
        self.dataSet = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.totalCount = params.get("totalCount")
        if params.get("dataSet") is not None:
            self.dataSet = []
            for item in params.get("dataSet"):
                obj = Member(item)
                self.dataSet.append(obj)


class Member(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.memberId = None
        self.userUid = None
        self.firstName = None
        self.lastName = None
        self.username = None
        self.assignmentStatus = None
        self.updateTime = None
        self.createTime = None

    def _deserialize(self, params):
        self.memberId = params.get("memberId")
        self.userUid = params.get("userUid")
        self.firstName = params.get("firstName")
        self.lastName = params.get("lastName")
        self.username = params.get("username")
        self.assignmentStatus = params.get("assignmentStatus")
        self.updateTime = params.get("updateTime")
        self.createTime = params.get("createTime")


class DescribeMemberRequest(AbstractModel):
    def __init__(self):
        self.userUid = None

    def _deserialize(self, params):
        self.userUid = params.get("userUid")


class DescribeMemberResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.memberId = None
        self.userUid = None
        self.firstName = None
        self.lastName = None
        self.username = None
        self.assignmentStatus = None
        self.updateTime = None
        self.createTime = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.memberId = params.get("memberId")
        self.userUid = params.get("userUid")
        self.firstName = params.get("firstName")
        self.lastName = params.get("lastName")
        self.username = params.get("username")
        self.assignmentStatus = params.get("assignmentStatus")
        self.updateTime = params.get("updateTime")
        self.createTime = params.get("createTime")


class InviteMemberRequest(AbstractModel):
    def __init__(self):
        self.email = None
        self.memberGroupId = None
        self.openApi = None

    def _deserialize(self, params):
        self.email = params.get("email")
        self.memberGroupId = params.get("memberGroupId")
        self.openApi = params.get("openApi")


class InviteMemberResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DeleteMemberRequest(AbstractModel):
    def __init__(self):
        self.userUid = None

    def _deserialize(self, params):
        self.userUid = params.get("userUid")


class DeleteMemberResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class SendInviteMemberEmailRequest(AbstractModel):
    def __init__(self):
        self.userUid = None

    def _deserialize(self, params):
        self.userUid = params.get("userUid")


class SendInviteMemberEmailResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeMemberGroupsRequest(AbstractModel):
    def __init__(self):
        self.name = None
        self.pageNum = None
        self.pageSize = None

    def _deserialize(self, params):
        self.name = params.get("name")
        self.pageNum = params.get("pageNum")
        self.pageSize = params.get("pageSize")


class DescribeMemberGroupsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.totalCount = None
        self.dataSet = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.totalCount = params.get("totalCount")
        if params.get("dataSet") is not None:
            self.dataSet = []
            for item in params.get("dataSet"):
                obj = MemberGroup(item)
                self.dataSet.append(obj)


class MemberGroup(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.memberGroupId = None
        self.name = None
        self.createTime = None

    def _deserialize(self, params):
        self.memberGroupId = params.get("memberGroupId")
        self.name = params.get("name")
        self.createTime = params.get("createTime")


class CreateMemberGroupRequest(AbstractModel):
    def __init__(self):
        self.name = None

    def _deserialize(self, params):
        self.name = params.get("name")


class CreateMemberGroupResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.memberGroupId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.memberGroupId = params.get("memberGroupId")


class ModifyMemberGroupRequest(AbstractModel):
    def __init__(self):
        self.name = None
        self.memberGroupId = None

    def _deserialize(self, params):
        self.name = params.get("name")
        self.memberGroupId = params.get("memberGroupId")


class ModifyMemberGroupResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DeleteMemberGroupRequest(AbstractModel):
    def __init__(self):
        self.memberGroupId = None

    def _deserialize(self, params):
        self.memberGroupId = params.get("memberGroupId")


class DeleteMemberGroupResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class CreateMemberGroupPermissionRequest(AbstractModel):
    def __init__(self):
        self.allResource = None
        self.resourceGroupId = None
        self.policies = None
        self.memberGroupId = None

    def _deserialize(self, params):
        self.allResource = params.get("allResource")
        self.resourceGroupId = params.get("resourceGroupId")
        self.policies = params.get("policies")
        self.memberGroupId = params.get("memberGroupId")


class CreateMemberGroupPermissionResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribePermissionsRequest(AbstractModel):
    def __init__(self):
        self.policyName = None
        self.resourceGroupName = None
        self.resourceGroupId = None
        self.userUid = None
        self.allResource = None
        self.memberGroupName = None
        self.memberGroupId = None
        self.associated = None
        self.order = None
        self.pageNum = None
        self.pageSize = None

    def _deserialize(self, params):
        self.policyName = params.get("policyName")
        self.resourceGroupName = params.get("resourceGroupName")
        self.resourceGroupId = params.get("resourceGroupId")
        self.userUid = params.get("userUid")
        self.allResource = params.get("allResource")
        self.memberGroupName = params.get("memberGroupName")
        self.memberGroupId = params.get("memberGroupId")
        self.associated = params.get("associated")
        self.order = params.get("order")
        self.pageNum = params.get("pageNum")
        self.pageSize = params.get("pageSize")


class DescribePermissionsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.totalCount = None
        self.dataSet = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.totalCount = params.get("totalCount")
        if params.get("dataSet") is not None:
            self.dataSet = []
            for item in params.get("dataSet"):
                obj = Permission(item)
                self.dataSet.append(obj)


class Permission(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.permissionId = None
        self.resourceGroupId = None
        self.allResource = None
        self.userUid = None
        self.createTime = None
        self.resourceGroupName = None
        self.policyId = None
        self.policyName = None
        self.policyDesc = None
        self.firstName = None
        self.lastName = None
        self.username = None
        self.memberGroupName = None
        self.memberGroupId = None
        self.associated = None

    def _deserialize(self, params):
        self.permissionId = params.get("permissionId")
        self.resourceGroupId = params.get("resourceGroupId")
        self.allResource = params.get("allResource")
        self.userUid = params.get("userUid")
        self.createTime = params.get("createTime")
        self.resourceGroupName = params.get("resourceGroupName")
        self.policyId = params.get("policyId")
        self.policyName = params.get("policyName")
        self.policyDesc = params.get("policyDesc")
        self.firstName = params.get("firstName")
        self.lastName = params.get("lastName")
        self.username = params.get("username")
        self.memberGroupName = params.get("memberGroupName")
        self.memberGroupId = params.get("memberGroupId")
        self.associated = params.get("associated")


class CreateMemberPermissionRequest(AbstractModel):
    def __init__(self):
        self.allResource = None
        self.resourceGroupId = None
        self.policies = None
        self.users = None

    def _deserialize(self, params):
        self.allResource = params.get("allResource")
        self.resourceGroupId = params.get("resourceGroupId")
        self.policies = params.get("policies")
        self.users = params.get("users")


class CreateMemberPermissionResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DeletePermissionRequest(AbstractModel):
    def __init__(self):
        self.permissionId = None

    def _deserialize(self, params):
        self.permissionId = params.get("permissionId")


class DeletePermissionResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribePoliciesRequest(AbstractModel):
    def __init__(self):
        pass

    def _deserialize(self, params):
        pass


class DescribePoliciesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.policies = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("policies") is not None:
            self.policies = []
            for item in params.get("policies"):
                obj = Policy(item)
                self.policies.append(obj)


class Policy(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.policyId = None
        self.allResource = None
        self.name = None
        self.desc = None
        self.authorizationTime = None

    def _deserialize(self, params):
        self.policyId = params.get("policyId")
        self.allResource = params.get("allResource")
        self.name = params.get("name")
        self.desc = params.get("desc")
        self.authorizationTime = params.get("authorizationTime")


class DescribeResourceGroupsRequest(AbstractModel):
    def __init__(self):
        pass

    def _deserialize(self, params):
        pass


class DescribeResourceGroupsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.resourceGroups = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("resourceGroups") is not None:
            self.resourceGroups = []
            for item in params.get("resourceGroups"):
                obj = ResourceGroup(item)
                self.resourceGroups.append(obj)


class ResourceGroup(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.resourceGroupId = None
        self.name = None
        self.createTime = None

    def _deserialize(self, params):
        self.resourceGroupId = params.get("resourceGroupId")
        self.name = params.get("name")
        self.createTime = params.get("createTime")


class CreateResourceGroupRequest(AbstractModel):
    def __init__(self):
        self.name = None

    def _deserialize(self, params):
        self.name = params.get("name")


class CreateResourceGroupResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.resourceGroupId = None
        self.name = None
        self.createTime = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.resourceGroupId = params.get("resourceGroupId")
        self.name = params.get("name")
        self.createTime = params.get("createTime")


class AddResourceResourceGroupRequest(AbstractModel):
    def __init__(self):
        self.resources = None
        self.resourceGroupId = None

    def _deserialize(self, params):
        self.resources = params.get("resources")
        self.resourceGroupId = params.get("resourceGroupId")


class AddResourceResourceGroupResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class ModifyResourceGroupRequest(AbstractModel):
    def __init__(self):
        self.name = None
        self.resourceGroupId = None

    def _deserialize(self, params):
        self.name = params.get("name")
        self.resourceGroupId = params.get("resourceGroupId")


class ModifyResourceGroupResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.resourceGroupId = None
        self.name = None
        self.createTime = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.resourceGroupId = params.get("resourceGroupId")
        self.name = params.get("name")
        self.createTime = params.get("createTime")


class DeleteResourceGroupRequest(AbstractModel):
    def __init__(self):
        self.resourceGroupId = None

    def _deserialize(self, params):
        self.resourceGroupId = params.get("resourceGroupId")


class DeleteResourceGroupResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


