#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.user.v20240529 import models
from zenlayercloud.common.abstract_client import AbstractClient


class UserClient(AbstractClient):
    _api_version = "2024-05-29"
    _service = "user"

    def DescribeMembers(self, request):
        """
        查询成员列表。用户可以根据名称、邮箱等信息来搜索成员信息。
        """
        response = self._api_call("DescribeMembers", request)
        model = models.DescribeMembersResponse()
        model._deserialize(response)
        return model

    def DescribeMember(self, request):
        """
        查询单个成员信息。
        """
        response = self._api_call("DescribeMember", request)
        model = models.DescribeMemberResponse()
        model._deserialize(response)
        return model

    def InviteMember(self, request):
        """
        邀请单个成员信息。
        """
        response = self._api_call("InviteMember", request)
        model = models.InviteMemberResponse()
        model._deserialize(response)
        return model

    def DeleteMember(self, request):
        """
        删除一个成员信息。
        """
        response = self._api_call("DeleteMember", request)
        model = models.DeleteMemberResponse()
        model._deserialize(response)
        return model

    def SendInviteMemberEmail(self, request):
        """
        重新发送一个成员信息的邮件。
        """
        response = self._api_call("SendInviteMemberEmail", request)
        model = models.SendInviteMemberEmailResponse()
        model._deserialize(response)
        return model

    def DescribeMemberGroups(self, request):
        """
        查询成员组列表。用户可以根据名称信息来搜索成员组信息。
        """
        response = self._api_call("DescribeMemberGroups", request)
        model = models.DescribeMemberGroupsResponse()
        model._deserialize(response)
        return model

    def CreateMemberGroup(self, request):
        """
        创建一个成员组。
        """
        response = self._api_call("CreateMemberGroup", request)
        model = models.CreateMemberGroupResponse()
        model._deserialize(response)
        return model

    def ModifyMemberGroup(self, request):
        """
        修改一个成员组信息。
        """
        response = self._api_call("ModifyMemberGroup", request)
        model = models.ModifyMemberGroupResponse()
        model._deserialize(response)
        return model

    def DeleteMemberGroup(self, request):
        """
        删除一个成员组信息。
        """
        response = self._api_call("DeleteMemberGroup", request)
        model = models.DeleteMemberGroupResponse()
        model._deserialize(response)
        return model

    def CreateMemberGroupPermission(self, request):
        """
        授予一个成员组相关访问策略信息，从而对进行成员组下所有成员进行权限控制。
        """
        response = self._api_call("CreateMemberGroupPermission", request)
        model = models.CreateMemberGroupPermissionResponse()
        model._deserialize(response)
        return model

    def DescribePermissions(self, request):
        """
        查询权限列表。用户可以根据成员ID、策略名称、成员组等信息来搜索权限信息。
        """
        response = self._api_call("DescribePermissions", request)
        model = models.DescribePermissionsResponse()
        model._deserialize(response)
        return model

    def CreateMemberPermission(self, request):
        """
        授予成员对于资源组相关的访问策略，从而对资源组进行权限控制。
        """
        response = self._api_call("CreateMemberPermission", request)
        model = models.CreateMemberPermissionResponse()
        model._deserialize(response)
        return model

    def DeletePermission(self, request):
        """
        删除一个权限信息。
        """
        response = self._api_call("DeletePermission", request)
        model = models.DeletePermissionResponse()
        model._deserialize(response)
        return model

    def DescribePolicies(self, request):
        """
        查询访问策略。
        """
        response = self._api_call("DescribePolicies", request)
        model = models.DescribePoliciesResponse()
        model._deserialize(response)
        return model

    def DescribeResourceGroups(self, request):
        """
        查询所有资源组列表信息。
        """
        response = self._api_call("DescribeResourceGroups", request)
        model = models.DescribeResourceGroupsResponse()
        model._deserialize(response)
        return model

    def CreateResourceGroup(self, request):
        """
        创建一个资源组信息。
        """
        response = self._api_call("CreateResourceGroup", request)
        model = models.CreateResourceGroupResponse()
        model._deserialize(response)
        return model

    def AddResourceResourceGroup(self, request):
        """
        将资源添加到一个资源组。
        """
        response = self._api_call("AddResourceResourceGroup", request)
        model = models.AddResourceResourceGroupResponse()
        model._deserialize(response)
        return model

    def ModifyResourceGroup(self, request):
        """
        修改一个资源组信息。
        """
        response = self._api_call("ModifyResourceGroup", request)
        model = models.ModifyResourceGroupResponse()
        model._deserialize(response)
        return model

    def DeleteResourceGroup(self, request):
        """
        删除一个资源组信息。
        """
        response = self._api_call("DeleteResourceGroup", request)
        model = models.DeleteResourceGroupResponse()
        model._deserialize(response)
        return model

