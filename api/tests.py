# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from rest_framework.test import APIClient
from myapp import models
import json


class APITests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.payload = {'age': 1, 'first_name': 'A', 'last_name': 'B'}
        self.person = models.Person.objects.create(age=10, fname='AA', lname='BB')

    def test_get(self):
        response = self.client.get('/api/person/%s/' % self.person.uuid).json()
        self.assertDictEqual({'first_name': 'AA', 'last_name': 'BB', 'age': 10}, response)

    def test_get_invalid_uuid(self):
        response = self.client.get('/api/person/%s/' % 123).json()
        self.assertDictEqual({'status': 'error', 'reason': 'Invalid UUID'}, response)

    def test_uuid_not_found(self):
        uuid = "%s0" % str(self.person.uuid)[:-1]
        response = self.client.get('/api/person/%s/' % uuid).json()
        self.assertDictEqual({'status': 'error', 'reason': 'UUID does not exist'}, response)


    def test_create_peron(self):
        response = self.client.put('/api/person/', data=json.dumps(self.payload), content_type='application/json').json()
        self.assertTrue(response['status'], 'ok')
        self.assertTrue('uuid' in response)

    def test_create_invalid_person(self):
        payload = dict(self.payload)
        del payload['first_name']
        response = self.client.put('/api/person/', data=json.dumps(payload), content_type='application/json').json()
        self.assertTrue(response['status'], 'error')
        self.assertTrue('reason' in response)

    def test_update_person(self):
        payload = dict(self.payload)
        del payload['first_name']
        del payload['last_name']
        payload['age'] = 100

        response = self.client.patch('/api/person/%s/' % self.person.uuid, data=json.dumps(payload), content_type='application/json').json()
        self.assertEqual(response['first_name'], self.person.fname)
        self.assertEqual(response['last_name'], self.person.lname)
        self.assertEqual(response['age'], 100)

        response = self.client.get('/api/person/%s/' % self.person.uuid).json()
        self.assertEqual(response['age'], 100)

        response = self.client.patch('/api/person/%s/' % self.person.uuid, data=json.dumps({"age":"abcd"}), content_type='application/json').json()
        self.assertEqual(response['status'], 'error')

    def test_patch_invalid_uuid(self):
        uuid = "%s0" % str(self.person.uuid)[:-1]
        response = self.client.patch('/api/person/%s/' % uuid).json()
        self.assertDictEqual({'status': 'error', 'reason': 'UUID does not exist'}, response)
        # Invalid payload
        response = self.client.patch('/api/person/%s/' % 123).json()
        self.assertDictEqual({'status': 'error', 'reason': 'Invalid UUID'}, response)

    def test_delete_uuid(self):
        response = self.client.delete('/api/person/%s/' % self.person.uuid).json()
        self.assertTrue(response['status'], 'ok')

    def test_delete_invalid_uuid(self):
        uuid = "%s0" % str(self.person.uuid)[:-1]
        response = self.client.delete('/api/person/%s/' % uuid).json()
        self.assertDictEqual({'status': 'error', 'reason': 'UUID does not exist'}, response)
        # Invalid payload
        response = self.client.delete('/api/person/%s/' % 123).json()
        self.assertDictEqual({'status': 'error', 'reason': 'Invalid UUID'}, response)