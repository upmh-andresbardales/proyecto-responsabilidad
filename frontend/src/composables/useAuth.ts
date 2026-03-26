/**
 * Composable de autenticación — conecta con el backend FastAPI.
 */

import { ref, computed } from 'vue'
import api from './useApi'

export interface AuthUser {
  username: string
  full_name: string
  email: string
  is_active: boolean
}

interface LoginResult {
  success: boolean
  message: string
  user: AuthUser | null
}

const currentUser = ref<AuthUser | null>(null)
const isAuthenticated = computed(() => currentUser.value !== null)

// Restaurar sesión desde sessionStorage al cargar
const stored = sessionStorage.getItem('auth_user')
if (stored) {
  try {
    currentUser.value = JSON.parse(stored)
  } catch {
    sessionStorage.removeItem('auth_user')
  }
}

export function useAuth() {
  async function login(username: string, password: string): Promise<LoginResult> {
    const { data } = await api.post<LoginResult>('/auth/login', { username, password })
    if (data.success && data.user) {
      currentUser.value = data.user
      sessionStorage.setItem('auth_user', JSON.stringify(data.user))
    }
    return data
  }

  function logout() {
    currentUser.value = null
    sessionStorage.removeItem('auth_user')
  }

  return { currentUser, isAuthenticated, login, logout }
}
